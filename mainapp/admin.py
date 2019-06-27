from django.contrib import admin

# Register your models here.
from . import models

class AnnouncementAdmin(admin.ModelAdmin):
    list_display=['text_string','time_of_announcement']
class MeetingAdmin(admin.ModelAdmin):
	list_display=['Agenda','time_of_meeting']
class DocumentsAdmin(admin.ModelAdmin):
	list_display=['name','the_file','type_of_doc']



admin.site.register(models.Announcement,AnnouncementAdmin)
admin.site.register(models.DocumentModel)
admin.site.register(models.Documents,DocumentsAdmin)
admin.site.register(models.Meeting,MeetingAdmin)
