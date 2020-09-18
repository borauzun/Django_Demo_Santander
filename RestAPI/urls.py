from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('helloWorld/', views.helloWorld),
    path('getId/<str:name>', views.getId),
    
    
]
