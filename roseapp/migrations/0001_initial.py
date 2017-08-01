# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 04:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obrands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Obrand_name', models.CharField(max_length=25, verbose_name='Brand')),
                ('Obrand_date', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Ocatergory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ocat_name', models.CharField(max_length=60, verbose_name='Catergory')),
                ('Ocat_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Catergory',
            },
        ),
        migrations.CreateModel(
            name='Ocountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocountry', models.CharField(max_length=50, verbose_name='Country')),
                ('ocountrydate', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Country',
            },
        ),
        migrations.CreateModel(
            name='Opacking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opacking_type', models.CharField(max_length=45, verbose_name='Packing')),
            ],
            options={
                'verbose_name': 'Packing',
            },
        ),
        migrations.CreateModel(
            name='opackingsize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ozpacking_size', models.PositiveIntegerField(default=0)),
                ('ozpacking_unit', models.PositiveIntegerField(default=0)),
                ('ozproduct_code', models.CharField(max_length=100)),
                ('oz_update_user', models.CharField(max_length=100)),
                ('oz_update_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Oproducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pd_name', models.CharField(max_length=250, verbose_name='Name')),
                ('pd_description', models.CharField(max_length=250, verbose_name='Description')),
                ('pd_image', models.CharField(max_length=200, verbose_name='Image')),
                ('pd_catid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseapp.Ocatergory', verbose_name='Catergory')),
                ('pd_obrandid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseapp.Obrands', verbose_name='Brand')),
                ('pd_ocountry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseapp.Ocountry', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Oshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oshop_name', models.CharField(max_length=50, verbose_name='Shop Name')),
                ('oshp_address', models.CharField(max_length=50, verbose_name='Address')),
                ('oshp_phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('oshp_person', models.CharField(max_length=50, verbose_name='Contact Person')),
                ('oshp_web', models.CharField(max_length=50, verbose_name='Www')),
                ('oshp_email', models.EmailField(max_length=240, verbose_name='Email')),
                ('oshp_locations', models.CharField(max_length=90, verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Shop',
            },
        ),
        migrations.CreateModel(
            name='Oshp_price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oshop_price', models.PositiveIntegerField(default=0, verbose_name='Price')),
                ('oprice_update_user', models.CharField(max_length=100)),
                ('oprice_update_date', models.DateTimeField(default=datetime.datetime.now)),
                ('oproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseapp.Oproducts', verbose_name='Product')),
                ('oshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseapp.Oshop', verbose_name='Shop')),
            ],
            options={
                'verbose_name': 'Shop Price',
            },
        ),
        migrations.CreateModel(
            name='Osubcatergory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osubcat', models.CharField(max_length=50, verbose_name='Sub Catergory')),
                ('ocatergory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseapp.Ocatergory')),
            ],
            options={
                'verbose_name': 'Sub Catergory',
            },
        ),
        migrations.AddField(
            model_name='oproducts',
            name='pd_subcatid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseapp.Osubcatergory', verbose_name='Sub Catergory'),
        ),
        migrations.AddField(
            model_name='opackingsize',
            name='oproduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseapp.Oproducts'),
        ),
        migrations.AddField(
            model_name='opackingsize',
            name='ozpacking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roseapp.Opacking'),
        ),
    ]
