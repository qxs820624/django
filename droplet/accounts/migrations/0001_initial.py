# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-13 03:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenstackAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeId', models.CharField(default='00000000', max_length=10, verbose_name='EmployeeId')),
                ('username', models.CharField(max_length=256, verbose_name='Name')),
                ('password', models.CharField(default='123456', max_length=256, verbose_name='Password')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='CreatedDate')),
                ('created_by', models.CharField(blank=True, max_length=256, null=True, verbose_name='CreatedBy')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='UpdatedDate')),
                ('updated_by', models.CharField(blank=True, max_length=256, null=True, verbose_name='UpdatedBy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'openstackaccount',
                'verbose_name_plural': 'openstackaccount',
            },
        ),
    ]
