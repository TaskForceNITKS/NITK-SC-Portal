# Generated by Django 2.2.2 on 2019-06-23 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_auto_20190623_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='time_of_announcement',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 6, 23, 22, 34, 5, 985095)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time_of_meeting',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 6, 23, 22, 34, 5, 985095)),
        ),
    ]
