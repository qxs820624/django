# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-13 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import draceditor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', draceditor.models.DraceditorField()),
            ],
        ),
    ]
