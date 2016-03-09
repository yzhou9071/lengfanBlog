# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20150807_1243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutauthordetail',
            options={'ordering': ['-authorDetailTime'], 'verbose_name': 'AuthorDetail', 'verbose_name_plural': 'AuthorDetails'},
        ),
        migrations.RemoveField(
            model_name='aboutauthordetail',
            name='authorDetailDes_markdown',
        ),
        migrations.RemoveField(
            model_name='aboutauthordetail',
            name='authorDetailDes_markup',
        ),
        migrations.AddField(
            model_name='aboutauthordetail',
            name='authorDetailFlag',
            field=models.IntegerField(default=0, help_text=' ', verbose_name='Detail Flag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aboutauthordetail',
            name='authorDetailHref',
            field=models.CharField(help_text=' ', max_length=255, verbose_name='Detail Href', blank=True),
            preserve_default=True,
        ),
    ]
