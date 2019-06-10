from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'app1/home.html')

def announcements(request):
    return render(request,'app1/announcements.html')

def club(request):
    return render(request,'app1/club.html')

def contact(request):
    return render(request,'app1/contact.html')


def documents(request):
    return render(request,'app1/documents.html')

def forms(request):
    return render(request,'app1/forms.html')


def grievances(request):
    return render(request,'app1/grievances.html')

def council(request):
    return render(request,'app1/council.html')

def meeting(request):
    return render(request,'app1/meeting.html')
