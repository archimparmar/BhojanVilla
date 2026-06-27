from django import forms
from .models import RoomBooking
from django.utils import timezone

class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = ['room', 'check_in', 'check_out', 'special_requests']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_check_in(self):
        check_in = self.cleaned_data['check_in']
        if check_in < timezone.now().date():
            raise forms.ValidationError("Check-in date cannot be in the past.")
        return check_in
