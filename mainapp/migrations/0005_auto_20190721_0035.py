# Generated by Django 2.2.2 on 2019-07-20 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20190628_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='time_of_announcement',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 7, 21, 0, 35, 47, 997044)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time_of_meeting',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 7, 21, 0, 35, 47, 997912)),
        ),
    ]
