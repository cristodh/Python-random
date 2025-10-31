from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Cliente
from .models import Mascota
from .serializers import ClienteSerializer
from .serializers import MascotaSerializer

# Create your views here
class ClienteCreateView(ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class MascotaCreateView(ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer