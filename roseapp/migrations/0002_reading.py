# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('weather', models.CharField(max_length=20)),
                ('wind_str', models.CharField(max_length=100)),
                ('temp', models.IntegerField()),
                ('humidity', models.CharField(max_length=10)),
                ('percip', models.CharField(max_length=50)),
                ('icon_url', models.CharField(max_length=100)),
                ('observation_time', models.CharField(max_length=100)),
            ],
        ),
    ]