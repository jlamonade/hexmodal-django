from rest_framework import serializers
from .models import Device, Payload


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"  # or an explicit list


class PayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payload
        fields = "__all__"  # or an explicit list
