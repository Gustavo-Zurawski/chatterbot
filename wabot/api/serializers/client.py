from ..models import Client
from rest_framework import serializers
from wabot.api.services.client_document import ClientDocumentModelService


class ClientModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'created_at', 'name', 'rg', 'issuing_body', 'uf', 'cpf',
                  'birth_date', 'local', 'issuance_date', 'face_coding']
        read_only_fields = ['created_at', 'id']


class ClientFaceRecognitionSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, default=None)

    class Meta:
        model = Client
        fields = ['image', 'id', 'created_at', 'name', 'rg', 'issuing_body', 'uf', 'cpf',
                  'birth_date', 'local', 'issuance_date']
        read_only_fields = ['id', 'created_at', 'name', 'rg', 'issuing_body', 'uf', 'cpf',
                            'birth_date', 'local', 'issuance_date', 'face_coding']

    def create(self, validated_data):
        image = validated_data.get('image').file
        client = ClientDocumentModelService.get_client_by_image(image)
        return client

    # def to_representation(self, instance):
    #     return super(ClientFaceRecognitionSerializer, self).to_representation(instance)
