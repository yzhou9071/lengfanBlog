# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20150808_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetail',
            name='bookState',
            field=models.IntegerField(default=0, help_text=' ', verbose_name='Book State'),
            preserve_default=True,
        ),
    ]
