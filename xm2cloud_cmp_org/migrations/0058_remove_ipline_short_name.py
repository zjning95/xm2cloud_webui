# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-04 08:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_cmp', '0057_ipline_band_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipline',
            name='short_name',
        ),
    ]