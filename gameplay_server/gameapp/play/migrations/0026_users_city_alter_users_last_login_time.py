# Generated by Django 4.0.3 on 2022-03-23 21:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0025_remove_users_city_alter_users_last_login_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='last_login_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 14, 39, 38, 520073)),
        ),
    ]