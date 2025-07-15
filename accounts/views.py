from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import RegisterForm

UserModel = get_user_model()

class RegisterView(CreateView):
    model = UserModel
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        print('GET called for RegisterView')  # DEBUG
        return super().get(request, *args, **kwargs)