from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'cameras', views.CameraViewSet)
router.register(r'logs', views.LogsViewSet)
router.register(r'dayroomstats', views.DayRoomStatsViewSet)

app_name = 'cam_api'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
