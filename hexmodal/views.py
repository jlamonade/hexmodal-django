from django.shortcuts import render
from rest_framework import viewsets

from .models import Device, Payload
from .serializers import DeviceSerializer, PayloadSerializer


# Create your views here.
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class PayloadViewSet(viewsets.ModelViewSet):
    queryset = Payload.objects.all()
    serializer_class = PayloadSerializer
