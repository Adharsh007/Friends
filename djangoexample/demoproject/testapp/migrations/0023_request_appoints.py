# Generated by Django 2.1.7 on 2019-04-30 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0022_auto_20190430_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='request_appoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('dateappoint', models.DateTimeField(auto_now_add=True)),
                ('ids', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.logins')),
            ],
        ),
    ]