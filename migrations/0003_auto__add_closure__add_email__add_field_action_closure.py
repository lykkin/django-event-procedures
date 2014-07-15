# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Closure'
        db.create_table(u'event_procedures_closure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'event_procedures', ['Closure'])

        # Adding model 'Email'
        db.create_table(u'event_procedures_email', (
            (u'closure_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['event_procedures.Closure'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'event_procedures', ['Email'])

        # Adding field 'Action.closure'
        db.add_column(u'event_procedures_action', 'closure',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_procedures.Closure'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Closure'
        db.delete_table(u'event_procedures_closure')

        # Deleting model 'Email'
        db.delete_table(u'event_procedures_email')

        # Deleting field 'Action.closure'
        db.delete_column(u'event_procedures_action', 'closure_id')


    models = {
        u'event_procedures.action': {
            'Meta': {'object_name': 'Action'},
            'closure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event_procedures.Closure']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event_procedures.Action']", 'null': 'True'})
        },
        u'event_procedures.closure': {
            'Meta': {'object_name': 'Closure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'event_procedures.email': {
            'Meta': {'object_name': 'Email', '_ormbases': [u'event_procedures.Closure']},
            u'closure_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['event_procedures.Closure']", 'unique': 'True', 'primary_key': 'True'})
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
