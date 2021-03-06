# Generated by Django 3.2.6 on 2021-09-03 07:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cam_api', '0003_auto_20210902_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayroomstats',
            name='day',
        ),
        migrations.RemoveField(
            model_name='dayroomstats',
            name='month',
        ),
        migrations.RemoveField(
            model_name='dayroomstats',
            name='week',
        ),
        migrations.RemoveField(
            model_name='dayroomstats',
            name='year',
        ),
        migrations.RemoveField(
            model_name='monthroomstats',
            name='month',
        ),
        migrations.RemoveField(
            model_name='monthroomstats',
            name='year',
        ),
        migrations.RemoveField(
            model_name='weekroomstats',
            name='month',
        ),
        migrations.RemoveField(
            model_name='weekroomstats',
            name='week',
        ),
        migrations.RemoveField(
            model_name='weekroomstats',
            name='year',
        ),
        migrations.RemoveField(
            model_name='yearroomstats',
            name='year',
        ),
        migrations.AddField(
            model_name='dayroomstats',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monthroomstats',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weekroomstats',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yearroomstats',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
