from django.contrib import admin

from hexmodal.models import Device, Payload


# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("devEUI", "name", "status", "created_at")
    search_fields = ("devEUI", "name", "description")
    list_filter = ("status", "created_at")


class PayloadAdmin(admin.ModelAdmin):
    list_display = ("fCnt", "devEUI", "created_at")
    search_fields = ("devEUI__devEUI", "devEUI__name")
    list_filter = ("created_at",)


admin.site.register(Device, DeviceAdmin)
admin.site.register(Payload, PayloadAdmin)