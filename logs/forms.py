from django import forms

from .models import TrafficRecord


class TrafficRecordForm(forms.ModelForm):
    class Meta:
        model = TrafficRecord
        fields = ["location", "date", "time", "vehicle_count", "condition"]
        widgets = {
            "location": forms.TextInput(
                attrs={"placeholder": "Enter location name"}
            ),
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "vehicle_count": forms.NumberInput(
                attrs={"placeholder": "Enter vehicle count", "min": "0"}
            ),
            "condition": forms.Select(),
        }

    def clean_location(self):
        return self.cleaned_data["location"].strip()
