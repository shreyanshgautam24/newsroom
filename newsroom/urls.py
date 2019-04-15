from django.urls import path
from . import views

app_name='newsroom'
urlpatterns = [
    path('newsroom/' ,views.newsroom,name='newsroom'),
    path('weather/',views.weather,name='weather'),

]
