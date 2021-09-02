from django.contrib.auth.models import User, Group
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import Room, Camera


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RoomIdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['id']


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'room_name')


class CameraSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    room = RoomIdSerializer()

    class Meta:
        model = Camera
        fields = ('id', 'room')