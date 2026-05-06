from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TrafficRecordForm
from .models import TrafficRecord


def home(request):
    records = TrafficRecord.objects.all()
    return render(request, "logs/home.html", {"records": records})


def add_record(request):
    if request.method == "POST":
        form = TrafficRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TrafficRecordForm()

    return render(request, "logs/add_record.html", {"form": form})


def delete_record(request, record_id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    record = get_object_or_404(TrafficRecord, id=record_id)
    record.delete()
    return redirect("home")
