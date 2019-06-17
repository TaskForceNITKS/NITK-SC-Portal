from django.db import models

# Create your models here.

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
