# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-14 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Город'),
        ),
    ]
