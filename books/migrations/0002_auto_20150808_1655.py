# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetail',
            name='bookDes',
            field=models.TextField(help_text=' ', verbose_name='Book Des'),
            preserve_default=True,
        ),
    ]
