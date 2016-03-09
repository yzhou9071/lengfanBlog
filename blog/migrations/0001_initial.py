# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=' ', max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(help_text='Uri identifier.', unique=True, max_length=255, verbose_name='Slug')),
                ('tags', models.CharField(help_text=' ', max_length=255, verbose_name='Tags')),
                ('content_markdown', models.TextField(help_text=' ', verbose_name='Content (Markdown)')),
                ('content_markup', models.TextField(help_text=' ', verbose_name='Content (Markup)')),
                ('pv', models.IntegerField(default=0, help_text=' ', verbose_name='PV')),
                ('publishDate', models.DateField(help_text=' ', verbose_name='Publish Date', auto_now_add=True)),
                ('publishTime', models.DateTimeField(help_text=' ', verbose_name='Publish Time', auto_now_add=True)),
                ('editTime', models.DateTimeField(help_text=' ', verbose_name='Edit Time', auto_now=True)),
            ],
            options={
                'ordering': ['-publishTime'],
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoryID', models.IntegerField(default=0, help_text=' ', verbose_name='ID')),
                ('title', models.CharField(help_text=' ', max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(help_text='Uri identifier.', unique=True, max_length=255, verbose_name='Slug')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(help_text=' ', to='blog.Category', null=True, verbose_name='Categories', blank=True),
            preserve_default=True,
        ),
    ]
