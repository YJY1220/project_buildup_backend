from django.contrib import admin
from django.urls import path, include
from rest_framework import urls
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('signup/', views.UserCreate.as_view()),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)