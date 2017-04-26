# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-30 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_auto_20161130_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudconsole',
            name='status',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Pending', 'Pending'), ('Active', 'Active')], default='Pending', max_length=32, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='package',
            name='status',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Pending', 'Pending'), ('Active', 'Active')], default='Pending', max_length=32, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='status',
            field=models.CharField(choices=[('Linux', 'Linux'), ('Windows', 'Windows')], default='Pending', max_length=32, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='type',
            field=models.CharField(choices=[('Linux', 'Linux'), ('Windows', 'Windows')], default='Linux', max_length=32, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='server',
            name='status',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Pending', 'Pending'), ('Active', 'Active')], default='Pending', max_length=32, verbose_name='Status'),
        ),
    ]
