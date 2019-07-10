# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=10, max_digits=10)),
                ('lon', models.DecimalField(decimal_places=10, max_digits=10)),
                ('place', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'geos',
            },
        ),
    ]
