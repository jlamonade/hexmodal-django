from django.test import TestCase

from hexmodal.models import Device
from hexmodal.serializers import PayloadSerializer


class DeviceTests(TestCase):
    def test_device_devEUI_character_limit(self):
        with self.assertRaises(Exception):
            Device.objects.create(
                devEUI="1234567890ABCDE",
                name="deviceA",
                status="failing",
            )

    def test_device_devEUI_uniqueness(self):
        Device.objects.create(
            devEUI="1234567890ABCDEF",
            name="deviceA",
            status="failing",
        )
        with self.assertRaises(Exception):
            Device.objects.create(
                devEUI="1234567890ABCDEF",
                name="deviceB",
                status="passing",
            )

    def test_device_invalid_status_failing_validation(self):
        with self.assertRaises(Exception):
            Device.objects.create(
                devEUI="1234567890ABCDEF",
                name="deviceA",
                status="invalid_status",
            )


class PayloadTests(TestCase):
    def setUp(self):
        self.device = Device.objects.create(
            devEUI="1234567890ABCDEF",
            name="deviceA",
            status="failing",
        )

    def _post_payload(self, fCnt, b64_str):
        serializer = PayloadSerializer(
            data={
                "fCnt": fCnt,
                "devEUI": self.device.pk,
                "data": b64_str,
                "rxInfo": {},
                "txInfo": {},
            }
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        serializer.save()

    def test_payload_with_data_01_marks_device_passing(self):
        self._post_payload(fCnt=1, b64_str="AQ==",)
        self.device.refresh_from_db()
        self.assertEqual(self.device.status, "passing")

    def test_fCnt_uniqueness_per_device(self):
        self._post_payload(fCnt=1, b64_str="AQ==",)
        with self.assertRaises(Exception):
            self._post_payload(fCnt=1, b64_str="AQ==",)

    def test_payload_with_non_01_data_marks_device_failing(self):
        self.device.status = "passing"
        self.device.save()
        self._post_payload(fCnt=2, b64_str="Ag==")
        self.device.refresh_from_db()
        self.assertEqual(self.device.status, "failing")

    def test_payload_with_invalid_base64_data_fails_validation(self):
        serializer = PayloadSerializer(
            data={
                "fCnt": 1,
                "devEUI": self.device.pk,
                "data": "invalid_base64",
                "rxInfo": {},
                "txInfo": {},
            }
        )
        self.assertFalse(serializer.is_valid())
        self.assertIn("data", serializer.errors)
