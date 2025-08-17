from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from gallery.mixins import GalleryLoginRequiredMixin
from gallery.models import Tattoo
from gallery.forms import TattooCreateForm


class TattooListView(GalleryLoginRequiredMixin, ListView):
    model = Tattoo
    template_name = 'gallery/tattoo-list.html'
    context_object_name = 'tattoos'
    paginate_by = 48

    def get_queryset(self):
        return Tattoo.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_items = list(context['page_obj'].object_list)
        context['left_tattoos'] = page_items[::2]
        context['right_tattoos'] = page_items[1::2]
        return context


class TattooCreateView(GalleryLoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Tattoo
    form_class = TattooCreateForm
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


class TattooBulkDeleteView(GalleryLoginRequiredMixin, UserPassesTestMixin, DeleteView):

    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, *args, **kwargs):
        ids = request.POST.getlist('ids')
        if not ids:
            messages.info(request, "No tattoos selected.")
            return redirect('tattoo-list')

        deleted, _ = Tattoo.objects.filter(id__in=ids).delete()
        messages.success(request, f"Deleted {len(ids)} tattoo(s).")
        return redirect('tattoo-list')

