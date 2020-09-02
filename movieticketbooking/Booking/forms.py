from django import forms
from Booking.models import booking
class bookingForms(forms.ModelForm):
    class Meta:
        model = booking
        fields = "__all__"