from rest_framework import serializers


class ChatterbotSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)