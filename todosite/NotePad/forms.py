from django import forms
from .models import NotePad


class NotePadForm(forms.ModelForm):
    class Meta:
        model = NotePad
        fields = "__all__"
