# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Email.subject'
        db.add_column(u'event_procedures_email', 'subject',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Email.message_html'
        db.add_column(u'event_procedures_email', 'message_html',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True),
                      keep_default=False)

        # Adding field 'Email.message_body'
        db.add_column(u'event_procedures_email', 'message_body',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Email.subject'
        db.delete_column(u'event_procedures_email', 'subject')

        # Deleting field 'Email.message_html'
        db.delete_column(u'event_procedures_email', 'message_html')

        # Deleting field 'Email.message_body'
        db.delete_column(u'event_procedures_email', 'message_body')


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
            'message_body': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'message_html': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
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
