# Generated by Django 4.0.3 on 2022-06-06 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0063_remove_landmarks_average_challenge_completion_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='allowable_distance_difference',
        ),
        migrations.RemoveField(
            model_name='cities',
            name='average_game_completion_time',
        ),
        migrations.AddField(
            model_name='chattanoogalandmarktimerecords',
            name='game_start',
            field=models.DecimalField(decimal_places=14, default=0.0, max_digits=24),
        ),
    ]
