from django import forms
from .models import Musician, Album


class MusicianCreateForm(forms.ModelForm):

    class Meta:
        model = Musician
        fields = "__all__"


class AlbumCreateForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = "__all__"
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }
