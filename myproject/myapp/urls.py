from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('faq/', views.faq),
    path('date/', views.display_date),
    path('message/', views.message),
]