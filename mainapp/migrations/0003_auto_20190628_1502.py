# Generated by Django 2.2.2 on 2019-06-28 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190628_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='time_of_announcement',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 6, 28, 15, 2, 23, 346789)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time_of_meeting',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 6, 28, 15, 2, 23, 346789)),
        ),
    ]