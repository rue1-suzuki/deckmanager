from app.models import Organizer
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CreateForm(UserCreationForm):
    class Meta:
        model = Organizer
        fields = ('username', 'password1', 'password2',)
        labels = {
            'username': 'ハンドルネーム(必須)',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'ルゥ@Rue1DM',
                },
            ),
        }


class UpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = Organizer
        fields = ('username',)
        labels = {
            'username': 'ハンドルネーム(必須)',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'ルゥ@Rue1DM',
                },
            ),
        }
