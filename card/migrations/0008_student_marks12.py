# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-11 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0007_auto_20180310_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_marks12',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(blank=True, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('term', models.CharField(blank=True, max_length=500, null=True)),
                ('grade', models.CharField(blank=True, max_length=500, null=True)),
                ('remark', models.CharField(blank=True, max_length=1000, null=True)),
                ('modified', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]