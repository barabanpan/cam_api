from django.contrib import admin

# for models to be modifiable in the admin
from .models import Room, Camera, Logs, DayRoomStats


admin.site.register(Room)
admin.site.register(Camera)
admin.site.register(Logs)
admin.site.register(DayRoomStats)
