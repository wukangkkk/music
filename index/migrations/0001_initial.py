# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('comment_text', models.CharField(max_length=500, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('comment_user', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7')),
                ('comment_date', models.CharField(max_length=50, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
            options={
                'verbose_name': '\u6b4c\u66f2\u8bc4\u8bba',
                'verbose_name_plural': '\u6b4c\u66f2\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('dynamic_id', models.AutoField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('dynamic_plays', models.IntegerField(verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe6\xac\xa1\xe6\x95\xb0')),
                ('dynamic_down', models.IntegerField(verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe6\xac\xa1\xe6\x95\xb0')),
                ('dynamic_search', models.IntegerField(verbose_name=b'\xe6\x94\xb6\xe6\x90\x9c\xe6\xac\xa1\xe6\x95\xb0')),
            ],
            options={
                'verbose_name': '\u6b4c\u66f2\u52a8\u6001',
                'verbose_name_plural': '\u6b4c\u66f2\u52a8\u6001',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('label_id', models.AutoField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('label_name', models.CharField(max_length=10, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\xa0\x87\xe7\xad\xbe')),
            ],
            options={
                'verbose_name': '\u6b4c\u66f2\u5206\u7c7b',
                'verbose_name_plural': '\u6b4c\u66f2\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('song_name', models.CharField(max_length=50, verbose_name=b'\xe6\xad\x8c\xe5\x90\x8d')),
                ('song_singer', models.CharField(max_length=50, verbose_name=b'\xe6\xad\x8c\xe6\x89\x8b')),
                ('song_time', models.CharField(max_length=10, verbose_name=b'\xe6\x97\xb6\xe9\x95\xbf')),
                ('song_album', models.CharField(max_length=50, verbose_name=b'\xe4\xb8\x93\xe8\xbe\x91')),
                ('song_languages', models.CharField(max_length=20, verbose_name=b'\xe8\xaf\xad\xe7\xa7\x8d')),
                ('song_type', models.CharField(max_length=20, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('song_release', models.CharField(max_length=20, verbose_name=b'\xe5\x8f\x91\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4')),
                ('song_img', models.CharField(max_length=20, verbose_name=b'\xe6\xad\x8c\xe6\x9b\xb2\xe5\x9b\xbe\xe7\x89\x87')),
                ('song_lyrics', models.CharField(default=b'\xe6\x9a\x82\xe6\x97\xa0\xe6\xad\x8c\xe8\xaf\x8d', max_length=50, verbose_name=b'\xe6\xad\x8c\xe8\xaf\x8d')),
                ('song_file', models.CharField(max_length=50, verbose_name=b'\xe6\xad\x8c\xe6\x9b\xb2\xe6\x96\x87\xe4\xbb\xb6')),
                ('label', models.ForeignKey(verbose_name=b'\xe6\xad\x8c\xe6\x9b\xb2\xe5\x88\x86\xe7\xb1\xbb', to='index.Label')),
            ],
            options={
                'verbose_name': '\u6b4c\u66f2\u4fe1\u606f',
                'verbose_name_plural': '\u6b4c\u66f2\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='dynamic',
            name='song',
            field=models.ForeignKey(verbose_name=b'\xe6\xad\x8c\xe5\x90\x8d', to='index.Song'),
        ),
        migrations.AddField(
            model_name='comment',
            name='song',
            field=models.ForeignKey(verbose_name=b'\xe6\xad\x8c\xe5\x90\x8d', to='index.Song'),
        ),
    ]
