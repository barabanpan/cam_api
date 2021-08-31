from django.contrib import admin

# for models to be modifiable in the admin
from .models import Room, Camera, Logs, DayRoomStats, WeekRoomStats, \
    MonthRoomStats, YearRoomStats 


admin.site.register(Room)
admin.site.register(Camera)
admin.site.register(Logs)
admin.site.register(DayRoomStats)
admin.site.register(WeekRoomStats)
admin.site.register(MonthRoomStats)
admin.site.register(YearRoomStats)
