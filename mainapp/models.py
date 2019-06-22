from django.db import models

import datetime
import os



class Announcement(models.Model):

    text_string=models.TextField()
    time_of_announcement=models.DateTimeField(datetime.datetime.now())


    def __str__(self):
        return self.text_string


class DocumentModel(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)


class Documents(models.Model):
    name = models.CharField(max_length=100)
    the_file = models.FileField(upload_to='mainapp.DocumentModel/bytes/filename/mimetype', blank=True, null=True)
    def __str__(self):
        return self.name



"""class Documents(models.Model):
    upload = models.FileField(upload_to=os.path.join('BASE_DIR','mainapp','Documents'))"""
