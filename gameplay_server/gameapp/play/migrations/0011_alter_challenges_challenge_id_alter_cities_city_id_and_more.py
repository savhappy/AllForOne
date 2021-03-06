# Generated by Django 4.0.3 on 2022-03-23 21:17

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0010_alter_challenges_challenge_id_alter_cities_city_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='challenge_id',
            field=models.UUIDField(default=uuid.UUID('8a3cac3e-dabb-4036-8f70-c1808943492f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cities',
            name='city_id',
            field=models.UUIDField(default=uuid.UUID('a07e871f-5e4d-4b01-a7f5-ddb67daa3f25'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='landmarks',
            name='landmark_id',
            field=models.UUIDField(default=uuid.UUID('e6a6a5c9-ecaa-40f3-a535-a4a77e4cddbb'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_login_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 14, 17, 6, 547324)),
        ),
    ]
