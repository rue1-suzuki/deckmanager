from app.models import Deck
from django import forms


class CreateForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ('number', 'name', 'image', 'remark', )
        labels = {
            'number': '識別番号(必須)',
            'name': 'ハンドルネーム(必須)',
            'image': 'デッキ画像(必須)',
            'remark': '備考',
        }
        widgets = {
            'number': forms.NumberInput(
                attrs={
                    'placeholder': '1',
                },
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'ルゥ@Rue1DM',
                },
            ),
            'remark': forms.Textarea(
                attrs={
                    'placeholder': '主催者からの指示があった場合に記入してください。\n',
                },
            ),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ('remark', )
        labels = {
            'remark': '備考',
        }
        widgets = {
            'remark': forms.Textarea(
                attrs={
                    'placeholder': '主催者からの指示があった場合に記入してください。\n',
                },
            ),
        }
