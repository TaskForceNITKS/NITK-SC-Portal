from team.models import Member
from django.core import serializers

Member.objects.all().delete()


with open('team/members_list/members.json') as data:
        for deserialized_object in serializers.deserialize("json", data):
            deserialized_object.save()