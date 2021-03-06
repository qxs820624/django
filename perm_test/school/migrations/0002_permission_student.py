# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-29 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u6743\u9650\u540d\u79f0')),
                ('url', models.CharField(max_length=255, verbose_name='URL\u540d\u79f0')),
                ('per_method', models.SmallIntegerField(choices=[(1, 'GET'), (2, 'POST')], default=1, verbose_name='\u8bf7\u6c42\u65b9\u6cd5')),
                ('argument_list', models.CharField(blank=True, help_text='\u591a\u4e2a\u53c2\u6570\u4e4b\u95f4\u7528\u82f1\u6587\u534a\u89d2\u9017\u53f7\u9694\u5f00', max_length=255, null=True, verbose_name='\u53c2\u6570\u5217\u8868')),
                ('describe', models.CharField(max_length=255, verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u6743\u9650\u8868',
                'verbose_name_plural': '\u6743\u9650\u8868',
                'permissions': (('views_student_list', '\u67e5\u770b\u5b66\u5458\u4fe1\u606f\u8868'), ('views_student_info', '\u67e5\u770b\u5b66\u5458\u8be6\u7ec6\u4fe1\u606f')),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u59d3\u540d')),
                ('age', models.SmallIntegerField(verbose_name='\u5e74\u9f84')),
                ('sex', models.SmallIntegerField(choices=[(1, '\u7537'), (2, '\u5973'), (3, '\u672a\u77e5')], verbose_name='\u6027\u522b')),
            ],
        ),
    ]
