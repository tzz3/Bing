from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('today/', views.today, name='today'),
    path('day/<int:day_id>/', views.day, name='day'),

]
