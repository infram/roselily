# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 07:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roseapp', '0003_oshp_price_oproduct_packingszie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oshp_price',
            name='oproduct_Packingszie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseapp.opackingsize', verbose_name='Packing'),
        ),
    ]
