from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('all/', views.get_all_events_page, name='get_all_events_page')
]