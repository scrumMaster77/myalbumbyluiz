# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 14:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_auto_20171125_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='egresado',
            name='foto',
        ),
    ]
