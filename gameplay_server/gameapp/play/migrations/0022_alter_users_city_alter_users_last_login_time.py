# Generated by Django 4.0.3 on 2022-03-23 21:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0021_users_city_users_last_login_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.cities'),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_login_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 14, 34, 44, 422434)),
        ),
    ]
