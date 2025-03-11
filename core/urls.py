from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView, RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/login/')),  # Redireciona para a tela de login
    path('index', TemplateView.as_view(template_name="index.html"), name='index'),
    path('email/', include('usuarios.urls')),
]
