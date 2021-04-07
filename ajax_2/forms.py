from django import forms
from .models import Student


class StudentRegistrationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ("__all__")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border border-dark', 'id': 'nameId', }),
            'email': forms.EmailInput(attrs={'class': 'border border-dark', 'id': 'emailId'}),
            'password': forms.PasswordInput(attrs={'class': 'border border-dark', 'id': 'passwordId', 'autocomplete': 'new-password'})
        }
