# Generated by Django 2.1.7 on 2019-04-30 09:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0024_auto_20190430_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='request_appointms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('appointdate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('ids', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.logins')),
            ],
        ),
    ]
