# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'event_procedures_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'event_procedures', ['Event'])

        # Adding model 'Action'
        db.create_table(u'event_procedures_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'event_procedures', ['Action'])

        # Adding model 'Procedure'
        db.create_table(u'event_procedures_procedure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_procedures.Event'], null=True)),
            ('root', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_procedures.Action'], null=True)),
        ))
        db.send_create_signal(u'event_procedures', ['Procedure'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'event_procedures_event')

        # Deleting model 'Action'
        db.delete_table(u'event_procedures_action')

        # Deleting model 'Procedure'
        db.delete_table(u'event_procedures_procedure')

    models = {
        u'event_procedures.action': {
            'Meta': {'object_name': 'Action'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'event_procedures.event': {
            'Meta': {'object_name': 'Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'event_procedures.procedure': {
            'Meta': {'object_name': 'Procedure'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event_procedures.Event']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'root': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event_procedures.Action']", 'null': 'True'})
        },
    }

    complete_apps = ['event_procedures']
