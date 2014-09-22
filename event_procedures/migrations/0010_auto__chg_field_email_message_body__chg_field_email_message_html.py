# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Email.message_body'
        db.alter_column(u'event_procedures_email', 'message_body', self.gf('django.db.models.fields.CharField')(default='sample.html', max_length=256))

        # Changing field 'Email.message_html'
        db.alter_column(u'event_procedures_email', 'message_html', self.gf('django.db.models.fields.CharField')(default='sample.html', max_length=256))

    def backwards(self, orm):

        # Changing field 'Email.message_body'
        db.alter_column(u'event_procedures_email', 'message_body', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Email.message_html'
        db.alter_column(u'event_procedures_email', 'message_html', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

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
            'closure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event_procedures.Closure']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'An unnamed action'", 'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event_procedures.Action']", 'null': 'True', 'blank': 'True'})
        },
        u'event_procedures.closure': {
            'Meta': {'object_name': 'Closure'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'An unnamed closure'", 'max_length': '100'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'})
        },
        u'event_procedures.email': {
            'Meta': {'object_name': 'Email'},
            'bcc': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cc': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_body': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'message_html': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'to': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
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
