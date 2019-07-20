from django.db import models

# Create your models here.
#All the activities are stored as models

class Crew(models.Model):

    SECTION_CHOICES = [
    (1, 'Technical Club'),
    (2, 'Cultural Club'),
    (3, 'Fest'),
    (4, 'Sports'),
    (None , 'Other'),
    ]

    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120)#Generally put as the head, convener, captain etc. of that group
    image = models.CharField(max_length=200, default="https://via.placeholder.com/800x400")
    description = models.TextField()
    section = models.PositiveSmallIntegerField(choices=SECTION_CHOICES, null=True, blank=True)#section denotes the type of group that each activity belogs to
