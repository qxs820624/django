# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-04 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20161102_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='perms',
            field=models.ManyToManyField(to='company.Permission'),
        ),
    ]
