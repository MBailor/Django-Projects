from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_contacts/', views.admin_contacts, name="admin_contacts"),
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('confirmDelete/', views.confirmed, name="confirmed"),
    path('createRecord/', views.createRecord, name="createRecord"),
    path('about/', views.about, name="about"),
]
