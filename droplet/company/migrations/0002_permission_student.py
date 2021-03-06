# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-29 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='permType')),
                ('url', models.CharField(max_length=255, verbose_name='URLName')),
                ('per_method', models.SmallIntegerField(choices=[(1, 'GET'), (2, 'POST')], default=1, verbose_name='method')),
                ('argument_list', models.CharField(blank=True, help_text='multiple arguments split by comma', max_length=255, null=True, verbose_name='paraList')),
                ('describe', models.CharField(max_length=255, verbose_name='description')),
            ],
            options={
                'verbose_name': 'table',
                'verbose_name_plural': 'table',
                'permissions': (('views_student_list', 'get information'), ('views_student_info', 'get detail')),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('age', models.SmallIntegerField(verbose_name='age')),
                ('sex', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'uncertain')], verbose_name='gender')),
            ],
        ),
    ]
