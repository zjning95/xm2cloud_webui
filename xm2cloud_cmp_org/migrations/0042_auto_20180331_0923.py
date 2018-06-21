# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-31 01:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_cmp', '0041_auto_20180329_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporttime', models.DateTimeField(auto_created=True, db_index=True, default=django.utils.timezone.now)),
                ('task_id', models.CharField(blank=True, default=uuid.UUID('78e94e6a-8321-416b-95c1-47e47cf7ac1f'), max_length=36)),
            ],
            options={
                'ordering': ['-reporttime'],
            },
        ),
        migrations.AddField(
            model_name='reporttask',
            name='clusters',
            field=models.ManyToManyField(to='xm2cloud_cmp.Cluster'),
        ),
        migrations.AddField(
            model_name='reporttask',
            name='contactgroups',
            field=models.ManyToManyField(to='xm2cloud_cmp.AlertContactGroup'),
        ),
        migrations.AddField(
            model_name='reporttask',
            name='fromdate',
            field=models.CharField(blank=True, choices=[('last_day', b'01:23_20180330'), ('last_week', b'01:23_20180330'), ('last_quarter', b'01:23_20180330'), ('last_year', b'01:23_20170429')], default='last_day', max_length=32),
        ),
        migrations.AddField(
            model_name='reporttask',
            name='hostgroups',
            field=models.ManyToManyField(to='xm2cloud_cmp.HostGroup'),
        ),
        migrations.AddField(
            model_name='reporttask',
            name='task_id',
            field=models.CharField(blank=True, default=uuid.UUID('f97b6905-5676-45ca-a340-666836b031e1'), max_length=36),
        ),
        migrations.AlterField(
            model_name='reporttask',
            name='reg_task',
            field=models.CharField(blank=True, choices=[(b'xm2cloud_cmp.tasks.report.running_report', b'xm2cloud_cmp.tasks.report.running_report')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='reporting',
            name='reporttask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xm2cloud_cmp.ReportTask'),
        ),
    ]