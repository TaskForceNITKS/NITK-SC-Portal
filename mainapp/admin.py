from django.contrib import admin

# Register your models here.
from . import models

class AnnouncementAdmin(admin.ModelAdmin):
    list_display=['text_string','time_of_announcement']



admin.site.register(models.Announcement,AnnouncementAdmin)
admin.site.register(models.DocumentModel)
admin.site.register(models.Documents)
