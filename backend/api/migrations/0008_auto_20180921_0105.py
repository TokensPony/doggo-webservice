# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-21 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_dog_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='color',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='favoritefood',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='favoritetoy',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='gender',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
