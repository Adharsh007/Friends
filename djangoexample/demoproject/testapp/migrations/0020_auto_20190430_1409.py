# Generated by Django 2.1.7 on 2019-04-30 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0019_request_appoint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request_appoint',
            name='ids',
        ),
        migrations.DeleteModel(
            name='request_appoint',
        ),
    ]
