# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Show.watch_state'
        db.alter_column('watchlist_show', 'watch_state', self.gf('django.db.models.fields.CharField')(default='', max_length=1))


    def backwards(self, orm):
        
        # Changing field 'Show.watch_state'
        db.alter_column('watchlist_show', 'watch_state', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))


    models = {
        'watchlist.show': {
            'Meta': {'ordering': "['title']", 'object_name': 'Show'},
            'encoding_group': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'production_type': ('django.db.models.fields.CharField', [], {'default': "'live action'", 'max_length': '12'}),
            'progress': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'watch_state': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        }
    }

    complete_apps = ['watchlist']
