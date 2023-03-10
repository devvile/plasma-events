
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tickets', views.tickets, name='tickets'),
    path('reg', views.regulations, name='reg'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('success', views.success, name='success'),
]
