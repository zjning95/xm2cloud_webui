# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-04 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_cmp', '0051_auto_20180404_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipline',
            name='short_name',
            field=models.CharField(max_length=32),
        ),
    ]