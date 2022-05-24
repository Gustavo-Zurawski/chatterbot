from ..models import Address
from rest_framework import serializers


class AddressModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'created_at', 'client', 'cep', 'street', 'number', 'district']
        read_only_fields = ['created_at', 'id']
