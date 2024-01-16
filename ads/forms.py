from django import forms
from .models import Ad, Response


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'content', 'category']


class ResponseForm(forms.ModelForm):
    text = forms.Textarea()

    class Meta:
        model = Response
        fields = ['text']
