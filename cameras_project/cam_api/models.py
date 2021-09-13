from django.db import models


class Room(models.Model):
    room_name = models.CharField(max_length=30)

    def __str__(self):
        return self.room_name


class Camera(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Logs(models.Model):
    date_time = models.DateTimeField()
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    n_people = models.IntegerField('number or people', default=0)


class DayRoomStats(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    max_people = models.IntegerField()
    max_time = models.DateTimeField()
    min_people = models.IntegerField()
    min_time = models.DateTimeField()
    avg_people = models.IntegerField()
