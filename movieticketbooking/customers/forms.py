from django import forms
from customers.models import customer
class customerForms(forms.ModelForm):
    class Meta:
        model = customer
        fields = "__all__"