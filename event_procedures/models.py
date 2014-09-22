from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.db import models
from django.template import Template, Context

from event_procedures.utils import extract_context_var

import importlib
import logging
import os


class Event(models.Model):
    name = models.CharField(max_length=50)

    def delete(self, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info("Deleting event: " + self.name)
        logger.info("and associated procedures:")
        for procedure in Procedure.objects.filter(event=self):
            procedure.delete()
        super(Event, self).delete(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Procedure(models.Model):
    event = models.ForeignKey('event_procedures.Event', null=True)
    root = models.ForeignKey('event_procedures.Action', null=True)

    @property
    def signal(self):
        module_name, _, class_name = self.event.name.rsplit('.', 2)
        return getattr(importlib.import_module(module_name).signals, class_name)

    def connect(self):
        logger = logging.getLogger(__name__)
        logger.info("Connecting " + str(self.root) + " to " + str(self.event))
        self.signal.connect(self.call, weak=False, dispatch_uid=str(self.id))

    def disconnect(self):
        logger = logging.getLogger(__name__)
        logger.info("Disconnecting " + str(self.root) + " from " + str(self.event))
        self.signal.disconnect(dispatch_uid=str(self.id))

    def save(self, *args, **kwargs):
        # When saved from django admin, the instance in memory
        # will have the new event loaded into memory, so we
        # must look up the previous version of the procedure
        # to disconnect it.
        try:
            Procedure.objects.get(id=self.id).disconnect()
        except Procedure.DoesNotExist:
            print "New procedure being created"
        super(Procedure, self).save(*args, **kwargs)
        self.connect()

    def delete(self, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info("Deleting procedure with id " + str(self.id) + "\
                     \nand associated with event " + str(self.event) + "\
                     \nand action " + str(self.root))
        self.disconnect()
        super(Procedure, self).delete(*args, **kwargs)

    def call(self, sender, **kwargs):
        kwargs.update({'sender': sender})
        self.root.call(**kwargs)

    def __unicode__(self):
        return "{} - {}".format(self.event, self.root)


class Action(models.Model):
    name = models.CharField(max_length=100, default="An unnamed action")
    parent = models.ForeignKey('event_procedures.Action', null=True, blank=True)

    closure = models.ForeignKey('event_procedures.Closure', null=True)

    @property
    def children(self):
        return list(Action.objects.filter(parent=self))

    def call(self, **kwargs):
        self.closure.call(**kwargs)
        for child in self.children:
            child.call(**kwargs)

    def __unicode__(self):
        return self.name


class Closure(models.Model):
    name = models.CharField(max_length=100, default="An unnamed closure")

    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    fn = generic.GenericForeignKey('content_type', 'object_id')

    def call(self, **kwargs):
        self.fn.call(**kwargs)

    def __unicode__(self):
        return self.name


class Email(models.Model):

    file_path = os.path.realpath(os.path.dirname(__file__)) + '/templates/'
    specs = [(path, files) for path, dirs, files in os.walk(file_path + 'email/') if not dirs]

    body_path, body_files = specs[0]
    body_file_paths = [body_path + '/' + file_name for file_name in body_files]
    BODY_CHOICES = zip(body_file_paths, body_files)

    html_path, html_files = specs[1]
    html_file_paths = [html_path + '/' + file_name for file_name in html_files]
    HTML_CHOICES = zip(html_file_paths, html_files)

    subject = models.CharField(max_length=100, null=True)
    message_html = models.CharField(max_length=256, choices=HTML_CHOICES)
    message_body = models.CharField(max_length=256, choices=BODY_CHOICES)
    to = models.CharField(max_length=50, null=True)
    cc = models.CharField(max_length=50, null=True, blank=True)
    bcc = models.CharField(max_length=50, null=True, blank=True)

    def prep_addresses(self, addresses, **kwargs):
        res = []
        addresses = [address for address in addresses if bool(address)]
        for address in addresses:
            address = address.strip()
            try:
                validate_email(address)
                res.append(address)
            except ValidationError:
                # invalid email, let's see if it is a deref from a
                # context variable
                extract_email = extract_context_var(address, kwargs)
                res.append(extract_email)
        return res

    def call(self, **kwargs):
        try:
            cc = self.prep_addresses(self.cc.split(';'), **kwargs) if self.cc is not None else None
            bcc = self.prep_addresses(self.bcc.split(';'), **kwargs) if self.bcc is not None else None
            to = self.prep_addresses(self.to.split(';'), **kwargs) if self.to is not None else None
        except LookupError as e:
            logger = logging.getLogger(__name__)
            logger.error("There was an error while parsing the email recipients:\n" + e)
            return
        with open(self.message_html) as html:
            message = Template(html.read())
        with open(self.message_body) as body:
            kwargs.update({
                'body': body.read()
            })
            context = Context(kwargs)
            message = message.render(context)
        EmailMessage(subject='subject', body=message, from_email=settings.AUTOMATED_EMAIL_ADDRESS,
                     to=to, bcc=bcc, cc=cc).send()
