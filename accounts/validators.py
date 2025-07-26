import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AppUserUsernameValidator:
    MIN_REQUIRED_LETTERS = 2

    def __init__(self, min_letters=MIN_REQUIRED_LETTERS):
        self._min_letters = min_letters


    @property
    def min_letters(self):
        return self._min_letters

    @min_letters.setter
    def min_letters(self, value):
        self._min_letters = value


    def __call__(self, username):

        if not username or not username.strip():
            raise ValidationError('Username must not be empty.')

        if not re.fullmatch(r'^[A-Za-z0-9_ ]+$', username):
            raise ValidationError('Username must contain only letters, digits, white spaces, and underscores.')

        if len(re.findall(r'[A-Za-z]', username)) < self._min_letters:
            raise ValidationError(f'Username must contain at least {self._min_letters} letters.')


@deconstructible
class BulgarianPhoneValidator:

    regex = re.compile(r'^\+359\d{9}$')
    message = (
        "Enter valid Bulgarian number: +359XXXXXXXXX "
    )

    def __call__(self, value):
        if not self.regex.match(value):
            raise ValidationError(self.message)


