# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photoTime', models.DateTimeField(auto_now_add=True, verbose_name='Photo Time')),
                ('photoTitle', models.CharField(max_length=255, verbose_name='Photo Title')),
                ('photoDes', models.CharField(max_length=255, verbose_name='Photo Des')),
            ],
            options={
                'ordering': ['-photoTime'],
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
            bases=(models.Model,),
        ),
    ]
