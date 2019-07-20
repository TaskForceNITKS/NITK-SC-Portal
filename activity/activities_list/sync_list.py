from activity.models import Crew
from django.core import serializers

Crew.objects.all().delete()


with open('activity/activities_list/activities.json') as data:
        for deserialized_object in serializers.deserialize("json", data):
            deserialized_object.save()
