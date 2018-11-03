from django.contrib import admin
from django.urls import path

from clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', views.ClienteList.as_view()),
    path('clientes/<int:pk>/', views.ClienteDetail.as_view())
]
