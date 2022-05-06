from ..models import Client
from rest_framework import serializers


class ClientModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'created_at', 'name', 'rg', 'issuing_body', 'uf', 'cpf',
                  'birth_date', 'local', 'issuance_date', 'face_coding']
        read_only_fields = ['created_at', 'id']
