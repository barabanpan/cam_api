from django.urls import path

from . import views

app_name = 'cam_api'
urlpatterns = [
    path('', views.index, name="index"),
    path('list_cameras/', views.list_cameras, name='list_cameras'),
    path('list_rooms/', views.list_rooms, name='list_rooms'),
    path('send_logs/', views.send_logs, name='send_logs'),
]