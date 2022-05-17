from ..models import Document
from rest_framework import serializers

from ..services.client_document import ClientDocumentModelService


class ClientDocumentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ['file', 'name', 'photo']
        read_only_fields = ['name']

    def create(self, validated_data):
        validated_data['name'] = validated_data.get('file').name
        document = super(ClientDocumentModelSerializer, self).create(validated_data)
        ClientDocumentModelService().process_data_by_document(document)
        return document

    def update(self, instance, validated_data):
        document = validated_data.get('document')
        client = ClientDocumentModelService().process_data_by_document(document)
        return client

    def to_representation(self, instance):
        return super(ClientDocumentModelSerializer, self).to_representation(instance)
