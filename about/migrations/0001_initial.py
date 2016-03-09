# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAuthorDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authorDetailDes', models.CharField(help_text=' ', max_length=255, verbose_name='Detail Des')),
                ('authorDetailDes_markdown', models.TextField(help_text=' ', verbose_name='Content (Markdown)')),
                ('authorDetailDes_markup', models.TextField(help_text=' ', verbose_name='Content (Markup)')),
                ('authorDetailTime', models.DateField(help_text=' ', verbose_name='Show Time')),
            ],
            options={
                'ordering': ['authorDetailTime'],
                'verbose_name': 'AuthorDetail',
                'verbose_name_plural': 'AuthorDetails',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AboutDownload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('downloadTitle', models.CharField(help_text=' ', max_length=255, verbose_name='Title')),
                ('downloadHref', models.CharField(help_text=' ', max_length=255, verbose_name='Href')),
                ('downloadTime', models.DateField(help_text=' ', verbose_name='Show Time')),
                ('downloadNum', models.IntegerField(default=0, help_text=' ', verbose_name='PV')),
            ],
            options={
                'ordering': ['downloadTime'],
                'verbose_name': 'Download',
                'verbose_name_plural': 'Downloads',
            },
            bases=(models.Model,),
        ),
    ]
