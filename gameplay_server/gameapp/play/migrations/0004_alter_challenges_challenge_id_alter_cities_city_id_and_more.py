# Generated by Django 4.0.3 on 2022-03-23 02:33

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0003_rename_city_id_users_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='challenge_id',
            field=models.UUIDField(default=uuid.UUID('a8253014-e670-4f2b-8817-ba343595401d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cities',
            name='city_id',
            field=models.UUIDField(default=uuid.UUID('fcd275be-1e59-43e7-ad08-343504ecfd9e'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='landmarks',
            name='landmark_id',
            field=models.UUIDField(default=uuid.UUID('e2d76a7b-3331-45f6-a792-7c601c4424b2'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_login_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 22, 19, 33, 40, 974386)),
        ),
    ]
