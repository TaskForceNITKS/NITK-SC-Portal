from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'mainapp/home.html')

def announcements(request):
    return render(request,'mainapp/announcements.html')

def club(request):
    return render(request,'mainapp/club.html')

def contact(request):
    return render(request,'mainapp/contact.html')


def documents(request):
    return render(request,'mainapp/documents.html')

def forms(request):
    return render(request,'mainapp/forms.html')


def grievances(request):
    return render(request,'mainapp/grievances.html')

def council(request):
    return render(request,'mainapp/council.html')

def meeting(request):
    return render(request,'mainapp/meeting.html')
