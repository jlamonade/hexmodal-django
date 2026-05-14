import base64
import binascii

from rest_framework import serializers

from .models import Device, Payload


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class PayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payload
        fields = "__all__"

    def validate_data(self, value: str) -> str:
        try:
            raw = base64.b64decode(value, validate=True)
        except (binascii.Error, ValueError):
            raise serializers.ValidationError("data must be a valid Base64 string")
        return raw.hex()
