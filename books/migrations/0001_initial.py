# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
                ('publisher', models.CharField(max_length=250)),
                ('published_date', models.CharField(max_length=250)),
            ],
        ),
    ]