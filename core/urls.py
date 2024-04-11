#######################################################
# Apps
# Tia Walker
# 04-09-24
#######################################################

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('exhibit/<str:pk>/', views.exhibit, name="exhibit"),
    path('exhibitlist/', views.exhibitlist, name='exhibitlist'),
    path('exhibitentry_test/', views.exhibitentry_test, name='exhibitentry_test'),
    path('send-data/', views.sendData, name="send-data"),
    path('play-info', views.playInfo, name = "play-info")
]