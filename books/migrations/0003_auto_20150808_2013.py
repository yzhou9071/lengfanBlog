# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20150808_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdetail',
            name='bookID',
        ),
        migrations.AlterField(
            model_name='bookdetail',
            name='bookTime',
            field=models.DateTimeField(help_text=' ', verbose_name='Collect Time', auto_now_add=True),
            preserve_default=True,
        ),
    ]
