
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import Profile

UserModel = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'password1', 'password2')
        labels = {
            'email': 'Email address',
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Repeat password',
        }
        help_texts = {
            'email': 'Enter a valid email address.',
            'username': 'Your username',
            'password1': 'Password',
            'password2': 'Repeat your password',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'example@domain.com',
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'username',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'password',
        })

        for field_name, field in self.fields.items():
            field.label = self.Meta.labels.get(field_name, field.label)
            field.help_text = self.Meta.help_texts.get(field_name, field.help_text)

class ProfileDetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'is_adult', 'tattoos_made', 'phone_number', 'social_media']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': '+3598XXXXXXXX'}),
            'social_media': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user and not user.is_staff:
            self.fields['tattoos_made'].disabled = True

