from accounts.models import AppUser, Profile
from django.http import HttpRequest
from typing import Optional

class ProfileAccessMixin:
    def get_object(self, queryset=None) -> Profile:
        request: Optional[HttpRequest] = getattr(self, 'request', None)
        user = request.user
        if isinstance(user, AppUser):
            return user.profile
        raise ValueError("No authenticated user.")