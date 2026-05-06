from django.test import TestCase
from django.urls import reverse

from .models import TrafficRecord


class TrafficRecordViewsTests(TestCase):
    def test_home_shows_empty_state(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No records yet")

    def test_add_record_saves_to_database(self):
        response = self.client.post(
            reverse("add_record"),
            {
                "location": "Pokhara",
                "date": "2026-05-06",
                "time": "08:00",
                "vehicle_count": 150,
                "condition": TrafficRecord.CONDITION_HEAVY,
            },
        )

        self.assertRedirects(response, reverse("home"))
        self.assertEqual(TrafficRecord.objects.count(), 1)
        record = TrafficRecord.objects.get()
        self.assertEqual(record.location, "Pokhara")

    def test_delete_record_removes_row(self):
        record = TrafficRecord.objects.create(
            location="Lakeside",
            date="2026-05-06",
            time="17:00",
            vehicle_count=200,
            condition=TrafficRecord.CONDITION_VERY_HEAVY,
        )

        response = self.client.post(reverse("delete_record", args=[record.id]))

        self.assertRedirects(response, reverse("home"))
        self.assertFalse(TrafficRecord.objects.filter(id=record.id).exists())
