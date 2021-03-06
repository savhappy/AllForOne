# Generated by Django 4.0.3 on 2022-03-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0048_users_active_game_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='total_game_completion_time',
            field=models.DecimalField(decimal_places=14, default=0.0, max_digits=24),
        ),
        migrations.AddField(
            model_name='cities',
            name='total_game_completions',
            field=models.IntegerField(default=1),
        ),
    ]
