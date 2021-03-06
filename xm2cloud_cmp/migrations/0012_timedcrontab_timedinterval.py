# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-15 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('djcelery', '0001_initial'),
        ('xm2cloud_cmp', '0011_timedtask_sevent_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimedCrontab',
            fields=[
                ('id', models.CharField(auto_created=True, default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('crontab', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='djcelery.CrontabSchedule')),
            ],
        ),
        migrations.CreateModel(
            name='TimedInterval',
            fields=[
                ('id', models.CharField(auto_created=True, default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('interval', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='djcelery.IntervalSchedule')),
            ],
        ),
    ]
