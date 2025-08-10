from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.http import urlencode


class GalleryLoginRequiredMixin(AccessMixin):
    login_url = reverse_lazy('gallery-please-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            next_url = request.get_full_path()
            login_prompt_url = f"{self.login_url}?{urlencode({'next': next_url})}"
            return redirect(login_prompt_url)

        return super().dispatch(request, *args, **kwargs)
