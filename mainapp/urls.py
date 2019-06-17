from django.urls import path,re_path,include

from . import views



urlpatterns=[
       path('',views.home,name='home'),
       path('forms/',views.forms,name='forms'),
       path('announcements/',views.announcements,name='announcements'),
       #path('know-your-council/',views.council,name='council'),
       path('contact-info/',views.contact,name='contact'),
       path('townhall-and-sc-meetings/',views.meeting,name='meeting'),
       path('grievances/',views.grievances,name='grievances'),
       path('clubs-and-calendar/',views.club,name='club'),
       path('documents/',views.documents,name='documents'),


]
