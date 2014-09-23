=======================
django-event-procedures
=======================

An event driven code execution system backed by Django

The idea of this is to have side-effectless code trees executing in response to a signal firing,
and being able to redefine what happens without touching the code.

Usage:
======
On Django's server start up, the signals specified in your settings will be pulled in and event objects
will be created in your db.  From there you can create new procedure objects that will call their action
trees when the related signals fire.

You can create your own code blocks to work with by creating a model with static vars as model fields
and local vars placed into kwargs. Note: the `call` method should accept only **kwargs as an argument
for homogeneity.


TODO:
=====
Allow for action chaining in a useful way.

Get some better organization going on for the closure models.

More docs/examples.

Hook into the startup hooks for later versions of Django; try to nix the middleware kludge anyway possible

Get white/blacklists for signals going on to cut out the problematic ones (e.g. infinite recursion
caused by model pre/post signals)


Getting started:
===============

Install:

        $ pip install django-event-procedures

In settings:


In INSTALLED_APPS add 'event_procedures' as such:

    INSTALLED_APPS = (
        ...
        'event_procedures',
        ...
    )
    
Somewhere in your settings files SIGNAL_MODULES as a list of modules containing 
the signals you want.
For example, if you want want django.core.signals it would look something like:

    SIGNAL_MODULES = [
        ...
        'django.core',
        ...
    ]
    
Register the event registration middleware in your middleware:

    MIDDLEWARE_CLASSES = (
        ...
        'event_procedures.middleware.EventRegistration',
        ...
    )
