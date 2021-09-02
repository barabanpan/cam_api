from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from .serializers import UserSerializer, GroupSerializer, RoomSerializer, CameraSerializer, LogsSerializer
from .models import Camera, Room, Logs


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = []


class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
    permission_classes = []


class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    permission_classes = []



def index(request):
    return HttpResponse("index page")


def list_rooms(request):
    rooms = Room.objects.all()
    return HttpResponse(rooms)


def list_cameras(request):
    cameras = Camera.objects.all()
    return HttpResponse(cameras)


def send_logs(request):  # make it post, how??
    # body = request.body
    return HttpResponse("body")
