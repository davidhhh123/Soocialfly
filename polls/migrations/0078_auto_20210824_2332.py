# Generated by Django 3.1.6 on 2021-08-24 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0077_profile_mes_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mes_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]