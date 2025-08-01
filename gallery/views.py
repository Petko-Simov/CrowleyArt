from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from gallery.mixins import GalleryLoginRequiredMixin
from gallery.models import Tattoo
from gallery.forms import TattooForm



class TattooListView(GalleryLoginRequiredMixin, ListView):
    model = Tattoo
    template_name = 'gallery/tattoo-list.html'
    context_object_name = 'tattoos'
    paginate_by = 10


class TattooCreateView(GalleryLoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Tattoo
    form_class = TattooForm
    template_name = 'gallery/tattoo-add.html'
    success_url = reverse_lazy('tattoo-list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('tattoo-list')

        return super().handle_no_permission()

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)
