# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Show'
        db.create_table('watchlist_show', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('encoding_group', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('watch_state', self.gf('django.db.models.fields.CharField')(max_length=1, null=True)),
            ('progress', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('watchlist', ['Show'])


    def backwards(self, orm):
        
        # Deleting model 'Show'
        db.delete_table('watchlist_show')


    models = {
        'watchlist.show': {
            'Meta': {'ordering': "['title']", 'object_name': 'Show'},
            'encoding_group': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'progress': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'watch_state': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'})
        }
    }

    complete_apps = ['watchlist']
