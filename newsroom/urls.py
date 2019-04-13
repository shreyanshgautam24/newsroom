from django.urls import path
from . import views

app_name='newsroom'
urlpatterns = [
    path('newsroom.html' ,views.newsroom,name='newsroom'),
    path('weather.html',views.weather,name='weather'),

]
