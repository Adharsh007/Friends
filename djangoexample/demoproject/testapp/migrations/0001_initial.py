# Generated by Django 2.1.7 on 2019-04-04 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorsid', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=30)),
                ('experience', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipmentid', models.CharField(max_length=40, unique=True)),
                ('equipmentname', models.CharField(max_length=100)),
                ('suppliername', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('billno', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='logins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicineid', models.CharField(max_length=40, unique=True)),
                ('medicinename', models.CharField(max_length=200)),
                ('suppliername', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('billno', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nurseid', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=30)),
                ('experience', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images')),
                ('ids', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.logins')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Collegeid', models.CharField(max_length=30, unique=True)),
                ('Name', models.CharField(max_length=50)),
                ('Designation', models.CharField(max_length=50)),
                ('Dob', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.CharField(max_length=50)),
                ('ids', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.logins')),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicineid', models.CharField(max_length=40, unique=True)),
                ('medicinename', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='feedbacks',
            name='ficollid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Register'),
        ),
        migrations.AddField(
            model_name='feedbacks',
            name='fimd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.logins'),
        ),
        migrations.AddField(
            model_name='doctors',
            name='ids',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.logins'),
        ),
    ]
