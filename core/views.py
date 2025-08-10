
from django.views.generic import TemplateView
from gallery.models import Tattoo


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tattoos = list(Tattoo.objects.order_by('-id'))
        context['left_tattoos'] = tattoos[::2]
        context['right_tattoos'] = tattoos[1::2]
        return context

