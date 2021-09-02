from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'cameras', views.CameraViewSet)
router.register(r'logs', views.LogsViewSet)

app_name = 'cam_api'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('', views.index, name="index"),
    path('list_cameras/', views.list_cameras, name='list_cameras'),
    path('list_rooms/', views.list_rooms, name='list_rooms'),
    path('send_logs/', views.send_logs, name='send_logs'),
]
