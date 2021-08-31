from django.http import HttpResponse

from .models import Camera, Room


def index(request):
	return HttpResponse("index page")


def list_rooms(request):
    rooms = Room.objects.all()
    return HttpResponse(rooms)


def list_cameras(request):
    cameras = Camera.objects.all()
    return HttpResponse(cameras)


def send_logs(request):  # make it post, how??
    #body = request.body
    return HttpResponse("body")
