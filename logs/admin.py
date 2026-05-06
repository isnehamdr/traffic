from django.contrib import admin

from .models import TrafficRecord


@admin.register(TrafficRecord)
class TrafficRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "location", "date", "time", "vehicle_count", "condition")
    list_filter = ("condition", "date")
    search_fields = ("location",)
