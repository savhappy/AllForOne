# Generated by Django 4.0.3 on 2022-03-23 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0002_rename_landmark_id_challenges_landmark_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='city_id',
            new_name='city',
        ),
        migrations.AlterField(
            model_name='users',
            name='last_login_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 22, 19, 29, 7, 818531)),
        ),
    ]
