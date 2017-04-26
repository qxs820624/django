# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-05 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='database',
            field=models.ManyToManyField(blank=True, to='applications.Database'),
        ),
        migrations.AlterField(
            model_name='product',
            name='language',
            field=models.ManyToManyField(blank=True, to='applications.ProgramLanguage'),
        ),
        migrations.AlterField(
            model_name='product',
            name='platform',
            field=models.ManyToManyField(blank=True, to='applications.Platform'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('ECOM', 'ECOM'), ('HealthCare', 'HealthCare'), ('Education', 'Education'), ('IoT', 'IoT'), ('CMS', 'CMS'), ('NoSQL', 'NoSQL'), ('DBMS', 'DBMS'), ('Artificial Intelligence', 'Artificial Intelligence')], default='DBMS', max_length=32, verbose_name='Type'),
        ),
    ]
