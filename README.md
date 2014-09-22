django-event-procedures
=======================

An event driven code execution system backed by django


Getting started:
===============

run:
    pip install django-event-procedures

in settings:
    In INSTALLED_APPS add 'event_procedures' as such:
        INSTALLED_APPS = (
            ...
            'event_procedures',
            ...
        )

    define SIGNAL_MODULES as a list of modules containing the signals you want
    For example, if you want want django.core.signals it would look something like
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
