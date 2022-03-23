# Generated by Django 4.0.3 on 2022-03-23 02:37

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0005_alter_challenges_challenge_id_alter_cities_city_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='challenge_id',
            field=models.UUIDField(default=uuid.UUID('2552f817-f9ca-47ca-bb61-dfc8a0468546'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cities',
            name='city_id',
            field=models.UUIDField(default=uuid.UUID('b560140f-aed9-4ecb-955e-b11106d8a526'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='landmarks',
            name='landmark_id',
            field=models.UUIDField(default=uuid.UUID('7f22897d-06b7-4a28-8349-605720b539c7'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_login_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 22, 19, 37, 26, 330260)),
        ),
    ]
