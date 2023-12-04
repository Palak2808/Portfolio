from django.contrib import admin
from django.urls import path
# from django.urls.conf import include

from main import views
urlpatterns = [
    path('',views.home),
    path('home',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('education',views.education,name='edu'),
    path('projects',views.projects,name='projects'),
    path('skills',views.skills,name='skills'),
    path('contact/',views.contact,name='contact'),
    path('resume/',views.resume,name='resume'),
   
]