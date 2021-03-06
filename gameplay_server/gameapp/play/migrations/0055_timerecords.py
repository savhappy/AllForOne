# Generated by Django 4.0.3 on 2022-03-26 03:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0054_delete_timerecords'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeRecords',
            fields=[
                ('time_record_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('completion_time', models.DecimalField(decimal_places=14, default=0.0, max_digits=24)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='play.cities')),
                ('landmark', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='play.landmarks')),
            ],
        ),
    ]
