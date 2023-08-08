from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.getImage),
    path('result',views.result),
    path('view',views.view)
]