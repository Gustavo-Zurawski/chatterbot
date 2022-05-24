from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser

from chatterbot.base.api_view import BaseModelViewSet
from ..serializers.client import ClientModelSerializer, ClientFaceRecognitionSerializer
from chatterbot.base.authentication import TokenAPIAuthentication


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


class ClientFaceRecognitionView(BaseModelViewSet):
    serializer_class = ClientFaceRecognitionSerializer
    parser_classes = [MultiPartParser]
    my_tags = ['Reconhecimento Facial Cliente']
    authentication_classes = [TokenAPIAuthentication]
    permission_classes = [IsAuthenticated, AllowAny]

