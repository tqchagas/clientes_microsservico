from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', views.ClienteCriarListar.as_view()),
    path('clientes/<int:pk>/', views.ClienteDetalheApagar.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
