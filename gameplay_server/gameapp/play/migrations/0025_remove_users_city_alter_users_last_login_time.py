# Generated by Django 4.0.3 on 2022-03-23 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0024_alter_users_city_alter_users_last_login_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='city',
        ),
        migrations.AlterField(
            model_name='users',
            name='last_login_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 14, 38, 15, 621419)),
        ),
    ]
