from django.shortcuts import render
from .models import Crew

# Create your views here.

def activities_view(request):
    q_tech_club = Crew.objects.filter(section=1)
    q_cul_club = Crew.objects.filter(section=2)
    q_fests = Crew.objects.filter(section=3)
    q_sports = Crew.objects.filter(section=4)
    q_other = Crew.objects.filter(section=None)

    context={
        'tech_club':q_tech_club,
        'cul_club':q_cul_club,
        'fests':q_fests,
        'sports':q_sports,
        'other':q_other,
    }

    return render(request, 'activities/activities.html' , context)
