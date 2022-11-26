from django import forms
from gallery.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('text', 'img')
