from django.urls import path, include
from django.views.generic import TemplateView
from gallery import views

urlpatterns = [
    path('', include([
        path('tattoos', views.TattooListView.as_view(), name='tattoo-list'),
        path('tattoos/bulk-delete/', views.TattooBulkDeleteView.as_view(), name='tattoo-bulk-delete'),
        path('add/', views.TattooCreateView.as_view(), name='tattoo-add'),
        path(
            'please-login/',
            TemplateView.as_view(template_name='gallery/login-or-register-prompt.html'),
            name='gallery-please-login'
        ),
    ])),
]
