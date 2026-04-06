from django import forms
from django.contrib.auth.models import User

from .models import FREQUENCIES


class ChainForm(forms.Form):
    name = forms.CharField(label="Streak Name")
    frequency = forms.ChoiceField(
        help_text="How offten will you will you do this?",
        choices=FREQUENCIES
    )
    frequency_count = forms.IntegerField(initial=1)
    is_active = forms.BooleanField(initial=True)


class NewUser(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean(self):
        data = super().clean()
        username = data.get("username")
        password1 = data.get("password1")
        password2 = data.get("password2")
        if username and User.objects.filter(username=username):
            self.add_error("username", f"The username {
                           username} already exsists.")
        if password1 != password2:
            self.add_error("password1", "Passwords did not match")
        return data
