# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_userinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Userinfo',
        ),
    ]
