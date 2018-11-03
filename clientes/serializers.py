from rest_framework import serializers
from clientes.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Cliente
