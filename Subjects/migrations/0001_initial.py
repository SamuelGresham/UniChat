# Generated by Django 3.2.6 on 2021-08-29 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_platform', models.CharField(max_length=50)),
                ('chat_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=50)),
                ('faculty_name', models.CharField(max_length=50)),
            ],
        ),
    ]