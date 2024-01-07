from django.urls import path
from . import views

urlpatterns=[
    path('', views.base),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.service, name='services'),
    path('coursesthird/',views.coursesthird,name='coursesthird'),
    path('result/',views.result,name='result'),
    path('firstcourses/',views.firstco,name='firstcourses'),
    path('firstresult/',views.firstresult,name='firstresult'),
    path('evensc/',views.evensc,name='evensc'),
    path('eresult/', views.Evenresult, name='eresult'),
    path('feedback/', views.feedback, name='feedback'),
    path('thankyou/', views.than, name='thankyou'),
    path('firsteven/', views.firsteven, name='firsteven'),
    ]