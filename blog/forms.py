from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder": "Email"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
        }


class TopicForm(forms.Form):
    topic = forms.CharField(
        max_length=120,
        label="Blog topic",
        widget=forms.TextInput(attrs={"placeholder": "Enter a blog topic"}),
    )
