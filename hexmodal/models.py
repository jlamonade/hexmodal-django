from django.db import models

DEVICE_STATUS_CHOICES = [
    ("passing", "Passing"),
    ("failing", "Failing"),
]


class Device(models.Model):
    devEUI = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=DEVICE_STATUS_CHOICES, default="passing")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Payload(models.Model):
    fCnt = models.IntegerField()
    devEUI = models.ForeignKey(Device, on_delete=models.CASCADE)
    data = models.CharField(max_length=512)
    rxInfo = models.JSONField()
    txInfo = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["devEUI", "fCnt"], name="unique_payload_per_device"),
        ]


    def __str__(self):
        return f"Payload for {self.devEUI} at {self.created_at}"
