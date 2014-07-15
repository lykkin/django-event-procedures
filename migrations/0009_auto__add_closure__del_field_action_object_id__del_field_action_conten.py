# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Closure'
        db.create_table(u'event_procedures_closure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='An unnamed closure', max_length=100)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
        ))
        db.send_create_signal(u'event_procedures', ['Closure'])

        # Deleting field 'Action.object_id'
        db.delete_column(u'event_procedures_action', 'object_id')

        # Deleting field 'Action.content_type'
        db.delete_column(u'event_procedures_action', 'content_type_id')

        # Adding field 'Action.closure'
        db.add_column(u'event_procedures_action', 'closure',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_procedures.Closure'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Closure'
        db.delete_table(u'event_procedures_closure')

        # Adding field 'Action.object_id'
        db.add_column(u'event_procedures_action', 'object_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Action.content_type'
        db.add_column(u'event_procedures_action', 'content_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True),
                      keep_default=False)

        # Deleting field 'Action.closure'
        db.delete_column(u'event_procedures_action', 'closure_id')


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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event_procedures.Action']", 'null': 'True'})
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
            'bcc': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'cc': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_body': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'message_html': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
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
