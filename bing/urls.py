from django.urls import path
from . import views

app_name = 'bing'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index2, name="index2"),
    path('today/', views.today, name='today'),
    path('day/<int:day_id>/', views.day, name='day'),
]
