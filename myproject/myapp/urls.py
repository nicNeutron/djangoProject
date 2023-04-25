from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('faq/', views.faq),
    path('date/', views.display_date),
    path('message/', views.message),
    path('dishes/<str:dish>', views.menuitems), # dish = cheesecake
    path('menu_item/10', views.menuitems),
    re_path(r'^menu_item/([0-9]{2})/$', views.menuitems),
]