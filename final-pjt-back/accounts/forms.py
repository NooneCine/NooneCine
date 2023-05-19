from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("name", "nickname")

    def signup(self, request, user):
        user.name = self.cleaned_data["name"]
        user.nickname = self.cleaned_data["nickname"]
        user.save()