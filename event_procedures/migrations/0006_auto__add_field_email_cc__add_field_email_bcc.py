# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Email.cc'
        db.add_column(u'event_procedures_email', 'cc',
                      self.gf('django.db.models.fields.EmailField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Email.bcc'
        db.add_column(u'event_procedures_email', 'bcc',
                      self.gf('django.db.models.fields.EmailField')(max_length=50, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Email.cc'
        db.delete_column(u'event_procedures_email', 'cc')

        # Deleting field 'Email.bcc'
        db.delete_column(u'event_procedures_email', 'bcc')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'event_procedures.action': {
            'Meta': {'object_name': 'Action'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event_procedures.Action']", 'null': 'True'})
        },
        u'event_procedures.email': {
            'Meta': {'object_name': 'Email'},
            'bcc': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'null': 'True'}),
            'cc': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'null': 'True'})
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
