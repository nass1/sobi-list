# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biz_list', '0010_auto_20170617_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='city',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
    ]
