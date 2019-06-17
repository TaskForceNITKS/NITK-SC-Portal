from django.db import models

# Create your models here.

#Each member of the student council is stored as a model. The data is loaded from the members.json file using a data migration(team/migrations/0002_auto_20190617_1307.py) when we run manage.py migrate.

class Member(models.Model):

    YEAR_IN_COLLEGE_CHOICES = [
    (1, 'First Year Btech'),
    (2, 'Second Year Btech'),
    (3, 'Third Year Btech'),
    (4, 'Fourth Year Btech'),
    (5, 'PG'),
    (6, 'PhD'),
    (None , 'Not Applicable'),
    ]
    
#The groups should be entered as either 'core','engineer','incident','cr-1','cr-2','cr-3','cr-4','cr-pg','cr-phd','phd-pg-advisory','acadamic-advisory','student-activites-advisory''sports-advisory','alumni-advisory','hostel-advisory','club-con','sports-cap','hostel-rep','alumni-coordinator'
#It is essential the group is entered correctly as it decides where the member is placed on the html page


    name = models.CharField(max_length=120, default="Quisquam Consectetur")
    post = models.CharField(max_length=120)
    group = models.CharField(max_length=120)
    email = models.EmailField(max_length=254, blank=True)
    year = models.PositiveSmallIntegerField(choices=YEAR_IN_COLLEGE_CHOICES, null=True, blank=True)
    image = models.CharField(max_length=200, default="https://via.placeholder.com/150")
    linkedin = models.CharField(max_length=200, default="#")
    facebook = models.CharField(max_length=200, default="#")
    phone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.post
