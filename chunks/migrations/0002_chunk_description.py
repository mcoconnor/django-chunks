# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chunks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chunk',
            name='description',
            field=models.CharField(blank=True, help_text='Short Description', max_length=64, verbose_name='Description'),
        ),
    ]
