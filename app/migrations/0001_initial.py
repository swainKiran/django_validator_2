# Generated by Django 5.0.3 on 2024-05-28 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sage', models.IntegerField()),
                ('semail', models.EmailField(max_length=254)),
                ('spassword', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('hobby', models.CharField(max_length=100)),
                ('school_type', models.CharField(max_length=50)),
                ('school_logo', models.FileField(upload_to='logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Guradian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=100)),
                ('gemail', models.EmailField(max_length=254)),
                ('gmob', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]