from genericadmin.admin import GenericAdminModelAdmin, GenericTabularInline
from django.contrib import admin

from event_procedures.models import Action, Closure, Email, Procedure


class ProcedureAdmin(admin.ModelAdmin):
    model = Procedure


class ClosureInline(GenericTabularInline):
    model = Closure
    ct_field = "content_type"
    ct_fk_field = "object_id"


class ClosureAdmin(GenericAdminModelAdmin):
    model = Closure
    content_type_whitelist = ('event_procedures/email')


class ActionAdmin(GenericAdminModelAdmin):
    model = Action
    content_type_whitelist = ('event_procedures/email')


class EmailAdmin(admin.ModelAdmin):
    model = Email

admin.site.register(Action, ActionAdmin)
admin.site.register(Closure, ClosureAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Procedure, ProcedureAdmin)
