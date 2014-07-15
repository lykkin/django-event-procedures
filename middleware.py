from event_procedures.models import Event, Procedure
from django.core.exceptions import MiddlewareNotUsed
from django.dispatch import Signal
from settings import SIGNAL_MODULES
import importlib


class EventRegistration(object):
    # Middleware used to force event population, this can probably be
    # replaced in versions 1.7+ by the start signal

    def __init__(self):
        signals = {}
        for module_str in SIGNAL_MODULES:
            module = importlib.import_module(module_str).signals
            sigs = {module_str + '.signals.' + name: getattr(module, name) for name in dir(module) if isinstance(getattr(module, name), Signal)}
            signals.update(sigs)

        names = [name for name, signal in signals.items()]
        Event.objects.exclude(name__in=names).delete()  # get rid of events we don't want
        event_names = [event.name for event in Event.objects.all()]
        new_names = [name for name in names if name not in event_names]  # add events that we want, but aren't tracking
        for name in new_names:
            Event.objects.create(name=name)

        for procedure in Procedure.objects.all():
            procedure.connect()

        raise MiddlewareNotUsed
