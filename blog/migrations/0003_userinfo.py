# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150622_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameCH', models.CharField(help_text=' ', max_length=255, verbose_name='Chinese Name')),
                ('nameEN', models.SlugField(help_text=' ', max_length=255, verbose_name='English Name')),
                ('startTime', models.DateTimeField(help_text=' ', verbose_name='start Time')),
                ('tags', models.CharField(help_text=' ', max_length=255, verbose_name='Tags')),
                ('birth', models.DateField(help_text=' ', verbose_name='Birthday', blank=True)),
                ('phone', models.CharField(help_text=' ', max_length=255, verbose_name='Phone Num', blank=True)),
                ('location', models.CharField(help_text=' ', max_length=255, verbose_name='Location', blank=True)),
                ('hometown', models.CharField(help_text=' ', max_length=255, verbose_name='Hometown', blank=True)),
                ('email', models.EmailField(help_text=' ', max_length=75, verbose_name='\u7535\u5b50\u90ae\u4ef6', blank=True)),
                ('qq', models.IntegerField(help_text=' ', verbose_name='QQ', blank=True)),
                ('wechat', models.CharField(help_text=' ', max_length=255, verbose_name='WeChat', blank=True)),
                ('weibo', models.CharField(help_text=' ', max_length=255, verbose_name='Weibo', blank=True)),
                ('github', models.CharField(help_text=' ', max_length=255, verbose_name='Github', blank=True)),
                ('rss', models.CharField(help_text=' ', max_length=255, verbose_name='RSS', blank=True)),
                ('investGame', models.CharField(help_text=' ', max_length=255, verbose_name='InvestGame', blank=True)),
                ('photo', models.ImageField(help_text=' ', upload_to=b'userPics', verbose_name='Photo', blank=True)),
                ('wechatCode', models.ImageField(help_text=' ', upload_to=b'userPics', verbose_name='WeChat Code', blank=True)),
                ('appCode', models.ImageField(help_text=' ', upload_to=b'userPics', verbose_name='App Code', blank=True)),
                ('moneyCode', models.ImageField(help_text=' ', upload_to=b'userPics', verbose_name='Money Code', blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
            bases=(models.Model,),
        ),
    ]
