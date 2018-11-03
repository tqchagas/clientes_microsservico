from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from rest_framework import generics


class ClienteCriarListar(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteDetalheApagar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
