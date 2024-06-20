from django import forms
from .models import ContactMessage, Call

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш вопрос',
            }),
        }

class CallForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['number']
        widgets = {
             'number': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width:220px',
                'placeholder': 'ваш телефон'
            }),
        }
