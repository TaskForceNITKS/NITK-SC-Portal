from django.urls import path,re_path,include

from . import views



urlpatterns=[
       path('',views.home,name='home'),
       path('forms/',views.forms,name='forms'),
       path('announcements/',views.AnnouncementsListView.as_view(),name='announcement_list'),
       #path('know-your-council/',views.council,name='council'),
       path('contact-info/',views.contact,name='contact'),
       path('townhall-and-sc-meetings/',views.meetingListView.as_view(),name='meeting_list'),
       path('grievances/',views.grievances,name='grievances'),
       path('clubs-and-calendar/',views.club,name='club'),
       path('documents/',views.DocumentsListView.as_view(),name='documents_list'),


]
