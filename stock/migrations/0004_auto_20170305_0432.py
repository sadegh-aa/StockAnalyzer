# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-05 04:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20170304_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='first_company',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='second_company',
        ),
        migrations.DeleteModel(
            name='Dashboard',
        ),
    ]
