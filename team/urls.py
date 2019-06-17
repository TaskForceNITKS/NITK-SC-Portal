from django.urls import path
from .views import council_view

app_name = 'team'
urlpatterns=[
    path('', council_view, name='council'),
]