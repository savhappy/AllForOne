# Generated by Django 4.0.3 on 2022-03-23 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0019_remove_users_id_users_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='city',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_login_time',
        ),
        migrations.RemoveField(
            model_name='users',
            name='public_key_address',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_name',
        ),
    ]
