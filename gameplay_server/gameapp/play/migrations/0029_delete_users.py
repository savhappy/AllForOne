# Generated by Django 4.0.3 on 2022-03-23 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0028_alter_users_last_login_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]