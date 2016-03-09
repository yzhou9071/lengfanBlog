# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bookName', models.CharField(help_text=' ', max_length=255, verbose_name='Book Name')),
                ('bookID', models.IntegerField(help_text=' ', verbose_name='Book ID')),
                ('bookAuthor', models.CharField(help_text=' ', max_length=255, verbose_name='Book Author')),
                ('bookProduct', models.CharField(help_text=' ', max_length=255, verbose_name='Book Product')),
                ('bookDes', models.CharField(help_text=' ', max_length=255, verbose_name='Book Des')),
                ('bookStar', models.CharField(help_text=' ', max_length=255, verbose_name='Book Star')),
                ('bookState', models.IntegerField(default=0, help_text=' ', verbose_name='Book ID')),
                ('bookFlag', models.BooleanField(default=False, help_text=' ', verbose_name='Book Flag')),
                ('bookHref', models.CharField(help_text=' ', max_length=255, verbose_name='Book Href', blank=True)),
                ('bookTime', models.DateField(help_text=' ', verbose_name='Collect Time')),
            ],
            options={
                'ordering': ['-bookTime'],
                'verbose_name': 'bookDetail',
                'verbose_name_plural': 'booksDetail',
            },
            bases=(models.Model,),
        ),
    ]
