# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-10 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_auto_20180309_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A1', models.IntegerField()),
                ('B1', models.IntegerField()),
                ('C1', models.IntegerField()),
                ('A2', models.IntegerField()),
                ('B2', models.IntegerField()),
                ('C2', models.IntegerField()),
                ('A3', models.IntegerField()),
                ('B3', models.IntegerField()),
                ('C3', models.IntegerField()),
                ('A4', models.IntegerField()),
                ('B4', models.IntegerField()),
                ('C4', models.IntegerField()),
                ('A5', models.IntegerField()),
                ('B5', models.IntegerField()),
                ('C5', models.IntegerField()),
                ('A6', models.IntegerField()),
                ('B6', models.IntegerField()),
                ('C6', models.IntegerField()),
                ('A7', models.IntegerField()),
                ('B7', models.IntegerField()),
                ('C7', models.IntegerField()),
                ('A8', models.IntegerField()),
                ('B8', models.IntegerField()),
                ('C8', models.IntegerField()),
            ],
        ),
    ]
