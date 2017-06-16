# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biz_list', '0007_about_social'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='social',
            new_name='facebook',
        ),
        migrations.AddField(
            model_name='about',
            name='google_plus',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='pin',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='snapchat',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='twitter',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='youtube',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='category',
            field=models.CharField(choices=[('Automotive', 'Automotive'), ('Education_Learning', 'Education & Learning'), ('Entertainment', 'Entertainment'), ('Financial_Services', 'Financial Services'), ('Hair_Beauty', 'Hair Beauty'), ('Medical', 'Medical'), ('Professional_Services', 'Professional Services'), ('Restaurants', 'Restaurants'), ('Retail_Shopping', 'Retail Shopping'), ('Sports_Recreation', 'Sports Recreation'), ('Trades_Services', 'Trades & Services'), ('Other', 'Other')], default='Automotive', max_length=100),
        ),
    ]
