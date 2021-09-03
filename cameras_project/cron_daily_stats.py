import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'cameras_project.settings'

import django
django.setup()


from datetime import datetime
from django.db.models import Avg

from cam_api.models import Room, Logs, DayRoomStats
from cam_api.constants import MISSING_VALUE


def compute_daily_stats(date=datetime.now()):
    # for every room in Room
    for room in Room.objects.all():
        stats = DayRoomStats(room=room, date_time=date)

        # get all logs for this room for today
        relevant_logs = Logs.objects.filter(
            camera__room__id=room.id,
            date_time__year=date.year,
            date_time__month=date.month,
            date_time__day=date.day
        )  # or date_time - now < 20 hours

        if len(relevant_logs) != 0:
            max_log = relevant_logs.order_by('-n_people')[0]
            min_log = relevant_logs.order_by('n_people')[0]

            stats.max_people = max_log.n_people
            stats.max_time = max_log.date_time
            stats.min_people = min_log.n_people
            stats.min_time = min_log.date_time
            stats.avg_people = relevant_logs.aggregate(Avg('n_people'))
        else:  # no logs for that period
            stats.max_people = MISSING_VALUE
            stats.max_time = date
            stats.min_people = MISSING_VALUE
            stats.min_time = date
            stats.avg_people = MISSING_VALUE

        stats.save()


if __name__ == "__main__":
    compute_daily_stats()
