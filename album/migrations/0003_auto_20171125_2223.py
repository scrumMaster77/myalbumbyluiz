# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20171125_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultad',
            name='nombre_nombre',
            field=models.CharField(default='facultad', max_length=400),
        ),
        migrations.AlterField(
            model_name='infoegresado',
            name='estado_civil',
            field=models.CharField(default='estado_civil', max_length=100),
        ),
        migrations.AlterField(
            model_name='infoegresado',
            name='estrato',
            field=models.CharField(default='estrato', max_length=4),
        ),
        migrations.AlterField(
            model_name='programa',
            name='nombre_programa',
            field=models.CharField(default='programa', max_length=400),
        ),
    ]
