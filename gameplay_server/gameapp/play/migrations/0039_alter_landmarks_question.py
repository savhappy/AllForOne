# Generated by Django 4.0.3 on 2022-03-23 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0038_landmarks_question_delete_challenges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmarks',
            name='question',
            field=models.CharField(default='', max_length=200),
        ),
    ]
