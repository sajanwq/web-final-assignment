from django import forms
from Admin.models import admin
class adminForms(forms.ModelForm):
    class Meta:
        model = admin
        fields = "__all__"