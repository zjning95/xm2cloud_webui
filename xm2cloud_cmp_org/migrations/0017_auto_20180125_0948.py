# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-25 01:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_cmp', '0016_remove_statuscheck_importance'),
    ]

    operations = [
        migrations.CreateModel(                                                                                                                                                      name='CheckHostResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],  
        ),
        migrations.AddField(
            model_name='checkhostresult',
            name='alert_status',
            field=models.CharField(choices=[('RELIEVED', '\u5df2\u89e3\u9664'), ('IGNORED', '\u5df2\u5ffd\u7565'), ('ALERTING', '\u544a\u8b66\u4e2d')], default='ALERTING', max_length=64),
        ),
        migrations.AddField(
            model_name='checkhostresult',
            name='check_result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='xm2cloud_cmp.StatusCheckResult'),
        ),
        migrations.AddField(
            model_name='checkhostresult',
            name='check_status',
            field=models.CharField(choices=[('CRITICAL', '\u4e25\u91cd'), ('PASSING', '\u6b63\u5e38'), ('WARNING', '\u8b66\u544a'), ('ERROR', '\u9519\u8bef')], default='PASSING', max_length=64),
        ),
        migrations.AddField(
            model_name='checkhostresult',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='checkhostresult',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='xm2cloud_cmp.Host'),
        ),
        migrations.AddField(
            model_name='checkhostresult',
            name='messages',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='checkhostresult',
            name='sta_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='checkhostresult',
            name='sub_metric',
            field=models.TextField(null=True),
        ),
    ]