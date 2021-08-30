from django.urls import path

from . import views

app_name = 'cam_api'
urlpatterns = [
    path('', views.index, name="index")
]