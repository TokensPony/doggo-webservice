# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_dog_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=1000),
        ),
    ]
