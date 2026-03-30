from django import forms

from .models import FREQUENCIES


class ChainForm(forms.Form):
    name = forms.CharField(label="Streak Name")
    frequency = forms.ChoiceField(
        help_text="How offten will you will you do this?",
        choices=FREQUENCIES
    )
    frequency_count = forms.IntegerField(initial=1)
    is_active = forms.BooleanField(initial=True)
