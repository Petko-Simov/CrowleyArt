from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MinLengthValidator

from accounts.models import Profile
from accounts.validators import AppUserUsernameValidator

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

    created_at = forms.DateTimeField(
        label="Created on:",
        required=False,
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',
            'class': 'form-control-plaintext text-light',
        })
    )

    username_input = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',
            'class': 'form-control-plaintext text-light',
        }),
    )

    is_adult = forms.CharField(
        label="Over 18 years old:",
        required=False,
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',
            'class': 'form-control-plaintext text-light',
        }),
    )

    class Meta:
        model = Profile

        fields = [
            'username_input',
            'tattoos_made',
            'phone_number',
            'social_media',
        ]
        widgets = {
            'tattoos_made': forms.NumberInput(attrs={
                'readonly': 'readonly',
                'class': 'form-control-plaintext text-light',
            }),
            'phone_number': forms.TextInput(attrs={
                'readonly': 'readonly',
                'class': 'form-control-plaintext text-light',
            }),
            'social_media': forms.URLInput(attrs={
                'readonly': 'readonly',
                'class': 'form-control-plaintext text-light',
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.nickname:
            self.fields['username_input'].initial = self.instance.nickname.username

        self.fields['is_adult'].initial = "Yes" if self.instance.is_adult else "No"

        self.fields['created_at'].initial = self.instance.created_at

        for name, field in self.fields.items():
            if name not in ('username_input', 'is_adult', 'created_at'):
                field.widget.attrs.update({
                    'readonly': 'readonly',
                    'class': 'form-control-plaintext text-light',
                })

        if user and not user.is_staff:
            self.fields['tattoos_made'].disabled = True



class ProfileEditForm(forms.ModelForm):
    username_input = forms.CharField(
        max_length=50,
        required=True,
        label="Nickname",
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        }
        ),
        validators=[
            AppUserUsernameValidator(),
            MinLengthValidator(2),
        ],
    )

    class Meta:
        model = Profile
        fields = [
            'username_input',
            'is_adult',
            'tattoos_made',
            'phone_number',
            'social_media',
        ]
        widgets = {
            'is_adult': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'tattoos_made': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': '+359XXXXXXXXX',
                'class': 'form-control',
            }),
            'social_media': forms.URLInput(attrs={
                'placeholder': 'https://...',
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.nickname:
            self.fields['username_input'].initial = self.instance.nickname.username

        if self.user and not self.user.is_staff:
            self.fields['tattoos_made'].disabled = True

    def save(self, commit=True):
        profile = super().save(commit=False)
        new_username = self.cleaned_data['username_input']
        user = profile.nickname
        user.username = new_username
        user.save()
        if commit:
            profile.save()

        return profile
