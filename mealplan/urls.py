from django.urls import path
from . import views

urlpatterns = [
    path('suggest-meal-plan/', views.suggest_meal_plan, name='suggest_meal_plan'),
]
