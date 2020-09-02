from django import forms
from movies.models import movie
class movieForms(forms.ModelForm):
    class Meta:
        model = movie
        fields = "__all__"