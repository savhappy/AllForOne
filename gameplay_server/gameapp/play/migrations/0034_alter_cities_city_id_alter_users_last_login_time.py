# Generated by Django 4.0.3 on 2022-03-23 22:01

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0033_alter_cities_city_id_alter_users_last_login_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='city_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_login_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 15, 1, 13, 535778)),
        ),
    ]
