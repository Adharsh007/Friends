# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-01 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0025_request_appointms'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Register')),
            ],
        ),
    ]
