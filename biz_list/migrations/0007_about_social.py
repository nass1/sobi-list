# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biz_list', '0006_remove_about_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='social',
            field=models.URLField(blank=True),
        ),
    ]