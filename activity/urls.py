from django.urls import path
from .views import activities_view
app_name = 'activity'
urlpatterns=[
    path('', activities_view, name='activities'),
]
