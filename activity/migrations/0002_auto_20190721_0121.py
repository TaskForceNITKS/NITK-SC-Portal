# Generated by Django 2.2.2 on 2019-07-20 19:51
import os
from django.db import migrations
from django.core import serializers
import json

def add_data(apps, schema_editor):
    with open('activity/activities_list/activities.json') as data:
        for deserialized_object in serializers.deserialize("json", data):
            deserialized_object.save()



class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]
