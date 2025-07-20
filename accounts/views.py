from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import RegisterForm, ProfileDetailsForm
from accounts.mixins import ProfileAccessMixin
from accounts.models import Profile, AppUser

UserModel = get_user_model()

class RegisterView(CreateView):
    model = UserModel
    form_class = RegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_success_url(self):
        return reverse('profile-details')


class ProfileDetailsView(LoginRequiredMixin, ProfileAccessMixin, DetailView):
    template_name = 'profile-details.html'
    context_object_name = 'profile'


class ProfileEditView(LoginRequiredMixin, ProfileAccessMixin, UpdateView):
    form_class = ProfileDetailsForm
    template_name = 'profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile-details')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ProfileDeleteView(LoginRequiredMixin, ProfileAccessMixin, DeleteView):
    template_name = 'profile-delete.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()
        return redirect(self.get_success_url())