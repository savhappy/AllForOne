# Generated by Django 4.0.3 on 2022-03-23 21:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0029_delete_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='city_id',
            field=models.UUIDField(default=uuid.UUID('17777417-2929-43c4-9530-3698802009a9'), editable=False, primary_key=True, serialize=False),
        ),
    ]
