from django import forms

from gallery.models import Tattoo


class TattooForm(forms.ModelForm):
    class Meta:
        model = Tattoo
        fields = [
            'tattoo_name',
            'artist',
            'image',
            'style',
            'description',
            'price',
        ]
        widgets = {
            'tattoo_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of the tattoo',
            }),
            'artist': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Artist name (optional)',
            }),
            'style': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Gothic, Realism',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Optional description',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Price',
            }),
        }