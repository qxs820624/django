# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-11 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0011_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudconsole',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Inactive', 'Inactive'), ('Active', 'Active')], default='Pending', max_length=32, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='package',
            name='memory',
            field=models.IntegerField(blank=True, choices=[(8, '8GB'), (2, '2GB'), (4, '4GB')], default=2, null=True, verbose_name='Memory'),
        ),
        migrations.AlterField(
            model_name='package',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Inactive', 'Inactive'), ('Active', 'Active')], default='Pending', max_length=32, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='package',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='UpdatedDate'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Inactive', 'Inactive'), ('Active', 'Active')], default='Pending', max_length=32, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='server',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Inactive', 'Inactive'), ('Active', 'Active')], default='Pending', max_length=32, verbose_name='Status'),
        ),
    ]
