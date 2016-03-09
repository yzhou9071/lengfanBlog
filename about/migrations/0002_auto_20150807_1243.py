# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutdownload',
            options={'ordering': ['-downloadTime'], 'verbose_name': 'Download', 'verbose_name_plural': 'Downloads'},
        ),
    ]
