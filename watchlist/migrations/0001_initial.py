# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('type', models.CharField(default=b'S', max_length=1, choices=[(b'M', b'Movie'), (b'S', b'Series')])),
                ('production_type', models.CharField(default=b'live action', max_length=12, choices=[(b'live action', b'Live-action'), (b'animated', b'Animated'), (b'anime', b'Anime')])),
                ('encoding_group', models.CharField(max_length=20, blank=True)),
                ('watch_state', models.CharField(blank=True, max_length=1, choices=[(b'N', b'Not Started'), (b'W', b'Watching'), (b'D', b'Done'), (b'L', b'Deferred'), (b'X', b'Dropped')])),
                ('progress', models.CharField(max_length=30, blank=True)),
                ('note', models.TextField(blank=True)),
                ('timestamp_created', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'added', auto_now_add=True)),
                ('timestamp_modified', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'last modified', auto_now=True)),
            ],
            options={
                'ordering': ['-timestamp_modified'],
            },
            bases=(models.Model,),
        ),
    ]
