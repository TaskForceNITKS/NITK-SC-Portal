# Generated by Django 2.2.2 on 2019-06-24 16:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0033_auto_20190624_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='time_of_announcement',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 6, 24, 21, 57, 3, 677944)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time_of_meeting',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 6, 24, 21, 57, 3, 678941)),
        ),
    ]
