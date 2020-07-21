from django.contrib import admin
from django.urls import path

from ToDoDashboard.views import index

urlpatterns = [
    path('', index)
]