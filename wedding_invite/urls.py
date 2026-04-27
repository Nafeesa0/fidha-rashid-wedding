from django.urls import path
from invitation import views

urlpatterns = [
    path('', views.envelope, name='envelope'),
    path('invite/', views.main_invite, name='main_invite'),
    path('rsvp/yes/', views.rsvp_yes, name='rsvp_yes'),
    path('rsvp/no/', views.rsvp_no, name='rsvp_no'),
]