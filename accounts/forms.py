
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

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
            'username': 'username',
            'password1': 'password',
            'password2': 'repeat password',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'example@domain.com',
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'your_username',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Repeat password',
        })

        for field_name, field in self.fields.items():
            field.label = self.Meta.labels.get(field_name, field.label)
            field.help_text = self.Meta.help_texts.get(field_name, field.help_text)
