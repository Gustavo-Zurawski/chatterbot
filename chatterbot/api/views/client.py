from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action, parser_classes
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser

from chatterbot.base.api_view import BaseModelViewSet
from ..serializers.client import ClientModelSerializer, ClientImageSerializer
from chatterbot.base.authentication import TokenAPIAuthentication
from chatterbot.api.services.client_document import ClientDocumentModelService


class ClientView(BaseModelViewSet):
    """
        create:
            <p>Cria novo cadastro de cliente.<p>
            <b>Funcionalidades:</b>
            <p>&ensp;&ensp;Salvar informações na base de dados;<p>

        retrieve:
            Retorna cliente filtrando pelo código.

        update:
            Atualizar CLiente.
            <n>
            <b>Parâmetros:</b>
            <b>&ensp;&ensp;id:</b> código referente cliente.
            <b>&ensp;&ensp;data:</b> json para atualização das informações.

        partial_update:
            Atualizar um ou mais campos em um CLiente.
            <n>
            <b>Parâmetros:</b>
            <b>&ensp;&ensp;id:</b> código referente ao cliente.
            <b>&ensp;&ensp;data:</b> json para atualização das informações.

        delete:
            Excluir Arquivo do Título.
            <n>
            <b>Parâmetro:</b>
            <b>&ensp;&ensp;id:</b> código referente ao cliente.

        relationship:
            Verifica se o registro possui vínculo com outro.
        """
    serializer_class = ClientModelSerializer
    my_tags = ['Cliente']
    authentication_classes = [TokenAPIAuthentication]
    permission_classes = [IsAuthenticated, AllowAny]

    class Meta:
        model = ClientModelSerializer.Meta.model

    @swagger_auto_schema(
        method='post',
        request_body=openapi.Schema(
            name='image',
            in_=openapi.IN_BODY,
            type=openapi.TYPE_FILE,
            format=openapi.FORMAT_BINARY,
            description="Document data"
        ),
    )
    @action(detail=False, methods=['POST'], url_path='by_image')
    @parser_classes([MultiPartParser])
    def get_client_by_image(self, request):
        """
        <p>Busca cliente por reconhecimento facial.<p>
        """
        image = request.data
        client = ClientDocumentModelService.get_client_by_image(image)
        return Response(client, status=status.HTTP_200_OK)
