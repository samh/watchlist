# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Show.timestamp_created'
        db.add_column('watchlist_show', 'timestamp_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 5, 21, 1, 47, 28, 481000), auto_now_add=True, blank=True), keep_default=False)

        # Adding field 'Show.timestamp_modified'
        db.add_column('watchlist_show', 'timestamp_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 5, 21, 1, 47, 28, 481000), auto_now=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Show.timestamp_created'
        db.delete_column('watchlist_show', 'timestamp_created')

        # Deleting field 'Show.timestamp_modified'
        db.delete_column('watchlist_show', 'timestamp_modified')


    models = {
        'watchlist.show': {
            'Meta': {'ordering': "['title']", 'object_name': 'Show'},
            'encoding_group': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'production_type': ('django.db.models.fields.CharField', [], {'default': "'live action'", 'max_length': '12'}),
            'progress': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'timestamp_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 21, 1, 47, 28, 481000)', 'auto_now_add': 'True', 'blank': 'True'}),
            'timestamp_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 21, 1, 47, 28, 481000)', 'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'watch_state': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        }
    }

    complete_apps = ['watchlist']
