# Generated by Django 4.0.3 on 2022-03-29 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0058_remove_users_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
