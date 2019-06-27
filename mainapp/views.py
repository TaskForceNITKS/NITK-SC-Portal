from django.shortcuts import render
from django.views.generic import ListView
from .models import Announcement,Meeting,Documents
# Create your views here.

def home(request):
    return render(request,'mainapp/home.html')



def club(request):
    return render(request,'mainapp/club.html')

def contact(request):
    return render(request,'mainapp/contact.html')


class DocumentsListView(ListView):
    model=Documents
    def get_queryset(self):
        return Documents.objects.all()
'''def documents(request):
    return render(request,'mainapp/documents_list.html')'''

def forms(request):
    return render(request,'mainapp/forms.html')


def grievances(request):
    return render(request,'mainapp/grievances.html')

def council(request):
    return render(request,'mainapp/council.html')

class meetingListView(ListView):
    model=Meeting
    def get_queryset(self):
        return Meeting.objects.all()


class AnnouncementsListView(ListView):
    model = Announcement

    def get_queryset(self):
        return Announcement.objects.all()
