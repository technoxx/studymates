# Generated by Django 4.2.3 on 2023-09-13 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_user_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
    ]
