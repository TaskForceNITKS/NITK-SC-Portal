from django.shortcuts import render
from django.views.generic import ListView
from .models import Announcement,Documents,Meeting

import json


from django.utils import timezone


def home(request):
    l=[]
    for object in Meeting.objects.all():
        if(object.time_of_meeting>timezone.now()):
            l.append(object)



    data={'announcement_list':(Announcement.objects.order_by('-time_of_announcement'))[:5],'meeting_list':l[:2]}
    return render(request,'mainapp/home.html',context=data)

def club(request):
    return render(request,'mainapp/club.html')

def contact(request):
    return render(request,'mainapp/contact.html')


class DocumentsListView(ListView):
    model=Documents
    def get_queryset(self):
        return Documents.objects.all()

def forms(request):
    return render(request,'mainapp/forms.html')


def grievances(request):
    return render(request,'mainapp/grievances.html')

def council(request):
    return render(request,'mainapp/council.html')


class AnnouncementsListView(ListView):
    model = Announcement

    def get_queryset(self):
        return Announcement.objects.order_by('-time_of_announcement')


class MeetingListView(ListView):
    model=Meeting
    def get_queryset(self):
        return Meeting.objects.order_by('time_of_meeting')
