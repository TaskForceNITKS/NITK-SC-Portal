from django.shortcuts import render
from .models import Member

# Create your views here.

def council_view(request):
    queryset = Member.objects.all()
    q_core = Member.objects.filter(group='core')
    q_engi = Member.objects.filter(group='engineer')
    q_inci = Member.objects.filter(group='incident')
    q_cr1 = Member.objects.filter(group='cr-1')
    q_cr2 = Member.objects.filter(group='cr-2')
    q_cr3 = Member.objects.filter(group='cr-3')
    q_cr4 = Member.objects.filter(group='cr-4')
    q_phd_pg_adv = Member.objects.filter(group='phd-pg-advisory')
    q_acad_adv = Member.objects.filter(group='acadamic-advisory')
    q_stud_act_adv = Member.objects.filter(group='student-activites-advisory')
    q_sports_adv = Member.objects.filter(group='sports-advisory')
    q_alumni_adv = Member.objects.filter(group='alumni-advisory')
    q_hostel_adv = Member.objects.filter(group='hostel-advisory')
    q_club_con = Member.objects.filter(group='club-con')
    q_sports_cap = Member.objects.filter(group='sports-cap')
    q_hostel_rep = Member.objects.filter(group='hostel-rep')
    q_alumni_coord = Member.objects.filter(group='alumni-coordinator')

    context={
        'object_list' : queryset,
        'core' : q_core,
        'inci' : q_inci,
        'engi' : q_engi,
        'cr1' : q_cr1,
        'cr2' : q_cr2,
        'cr3' : q_cr3,
        'cr4' : q_cr4,
        'phd_pg_adv' : q_phd_pg_adv,
        'acad_adv' : q_acad_adv,
        'stud_act_adv' : q_stud_act_adv,
        'alumni_adv' : q_alumni_adv,
        'sports_adv' : q_sports_adv,
        'hostel_adv' : q_hostel_adv,
        'club_con' : q_club_con,
        'sports_cap' : q_sports_cap,
        'hostel_rep' : q_hostel_rep,
        'alumni_coord' : q_alumni_coord,
        

    }
    return render(request, 'team/council.html' , context)