from django.db import models


class TrafficRecord(models.Model):
    CONDITION_NORMAL = "Normal"
    CONDITION_MEDIUM = "Medium"
    CONDITION_HEAVY = "Heavy"
    CONDITION_VERY_HEAVY = "Very Heavy"

    CONDITION_CHOICES = [
        (CONDITION_NORMAL, "Normal"),
        (CONDITION_MEDIUM, "Medium"),
        (CONDITION_HEAVY, "Heavy"),
        (CONDITION_VERY_HEAVY, "Very Heavy"),
    ]

    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    vehicle_count = models.PositiveIntegerField()
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)

    class Meta:
        ordering = ["date", "time", "id"]

    def __str__(self):
        return f"{self.location} - {self.date}"
