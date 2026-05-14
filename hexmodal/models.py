from django.db import models

DEVICE_STATUS_CHOICES = [
    ("passing", "Passing"),
    ("failing", "Failing"),
]
PASSING_DATA = "01"


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        new_status = "passing" if self.data == PASSING_DATA else "failing"
        self.devEUI.status = new_status  # safe since DRF catches invalid devEUI before save
        self.devEUI.save()

    def __str__(self):
        return f"Payload for {self.devEUI} at {self.created_at}"
