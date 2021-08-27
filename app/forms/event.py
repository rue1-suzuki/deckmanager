from app.models import Event
from django import forms


class CreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'date', 'message', 'is_active', )
        labels = {
            'title': 'イベント名(必須)',
            'date': '開催日(必須)',
            'message': '参加者へのメッセージ(任意)',
            'is_active': '状態',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': '第1回 DM秋田CS【アドバンス】',
                },
            ),
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                },
            ),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('is_active', )
        labels = {
            'is_active': '状態',
        }
