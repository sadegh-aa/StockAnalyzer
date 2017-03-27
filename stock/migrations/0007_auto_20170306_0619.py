# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-06 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20170306_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardinfo',
            name='dashboard_chart_type',
            field=models.CharField(choices=[('line', 'line'), ('pie', 'pie'), ('scatter', 'scatter'), ('column', 'column')], max_length=100),
        ),
        migrations.AlterField(
            model_name='dashboardinfo',
            name='dashboard_chart_xaxis',
            field=models.CharField(choices=[('stock_volume', 'stock_volume'), ('stock_date', 'stock_date'), ('stock_low', 'stock_low'), ('stock_high', 'stock_high'), ('stock_close', 'stock_close'), ('stock_open', 'stock_open')], max_length=200),
        ),
    ]
