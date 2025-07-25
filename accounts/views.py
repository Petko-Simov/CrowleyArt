from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import RegisterForm, ProfileEditForm, ProfileDetailsForm
from accounts.mixins import ProfileAccessMixin
from accounts.models import Profile

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


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return Profile.objects.get(nickname=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProfileDetailsForm(instance=self.get_object())
        return context


class ProfileEditView(LoginRequiredMixin, ProfileAccessMixin, UpdateView):
    form_class = ProfileEditForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProfileDetailsForm(instance=self.get_object(), user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()
        return redirect(self.get_success_url())