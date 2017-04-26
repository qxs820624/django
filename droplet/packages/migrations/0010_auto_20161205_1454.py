# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-05 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0009_auto_20161130_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='status',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Active', 'Active'), ('Pending', 'Pending')], default='Pending', max_length=32, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='type',
            field=models.CharField(choices=[('Linux', 'Linux'), ('Windows', 'Windows')], default='Linux', max_length=32, verbose_name='Type'),
        ),
    ]