# Generated by Django 4.0.3 on 2022-03-26 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0053_alter_timerecords_city_alter_timerecords_landmark'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TimeRecords',
        ),
    ]
