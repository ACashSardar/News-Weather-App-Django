from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ChannelNews, name="ChannelNews"),
    path('CategoryNews/<str:category>',views.CategoryNews, name="CategoryNews"),
    path('Weather/',views.Weather, name="Weather"),
    path('Livenews/',views.Livenews, name="Livenews"),
]