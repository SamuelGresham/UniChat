# Generated by Django 3.2.6 on 2021-08-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0006_alter_chat_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='mess_id',
            field=models.CharField(default='', max_length=20),
        ),
    ]
