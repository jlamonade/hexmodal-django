from django.db import models

# Create your models here.
DEVICE_STATUS_CHOICES = [
    ("passing", "Passing"),
    ("failing", "Failing"),
]


class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=DEVICE_STATUS_CHOICES, default="passing")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Payload(models.Model):
    fCnt = models.IntegerField(primary_key=True, unique=True, editable=False)  # message counter, unique and auto-incrementing
    deviceEUI = models.CharField(foreign_key=Device, max_length=16)  # foreign key to Device model
    data = models.TextField()  # raw payload data
    rxInfo = models.JSONField()  # JSON field to store rxInfo array
    txInfo = models.JSONField()  # JSON field to store txInfo object
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payload for {self.deviceEUI} at {self.created_at}"
