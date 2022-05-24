import json

from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from chatterbot import ChatBot
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from ..serializers.chatterbot import ChatterbotSerializer


class ChatterBotApiView(ViewSet):
    my_tags = ['Chatterbot']
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    @swagger_auto_schema(method='post', request_body=ChatterbotSerializer)
    @action(
        detail=False,
        methods=['post'],
        url_path='create',
        url_name='create',
        name='Post teste'
    )
    def post(self, request):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    @swagger_auto_schema(method='get')
    @action(detail=False, methods=['get'], url_path='', url_name='', name='Get')
    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
