from django.core.validators import RegexValidator
from django.db import models

DEV_EUI_VALIDATOR = RegexValidator(
    regex=r"^[0-9a-fA-F]{16}$",
    message="DevEUI must be exactly 16 hexadecimal characters.",
)

PASSING_DATA = "01"


class DeviceStatusChoices(models.TextChoices):
    PASSING = "passing", "Passing"
    FAILING = "failing", "Failing"


class Device(models.Model):
    devEUI = models.CharField(
        max_length=16, primary_key=True, validators=[DEV_EUI_VALIDATOR]
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=DeviceStatusChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Payload(models.Model):
    fCnt = models.IntegerField()
    devEUI = models.ForeignKey(Device, on_delete=models.CASCADE)
    data = models.CharField(max_length=512)
    rxInfo = models.JSONField()
    txInfo = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["devEUI", "fCnt"], name="unique_payload_per_device"
            ),
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        new_status = "passing" if self.data == PASSING_DATA else "failing"
        self.devEUI.status = (
            new_status  # safe since DRF catches invalid devEUI before save
        )
        self.devEUI.save()

    def __str__(self):
        return f"Payload for {self.devEUI} at {self.created_at}"
