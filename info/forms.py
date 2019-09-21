from django import forms
from .models import BloodInfo


class BloodInfoForm(forms.ModelForm):

    class Meta:
        model = BloodInfo
        exclude = []
