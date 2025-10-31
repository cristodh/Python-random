from django.urls import path
from .views import ClienteCreateView
from .views import MascotaCreateView

urlpatterns = [
    path('crear-cliente/',ClienteCreateView.as_view())
]

urlpatterns = [
    path('crear-mascota/',MascotaCreateView.as_view())
]