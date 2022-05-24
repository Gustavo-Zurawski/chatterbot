from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser

from wabot.base.api_view import BaseModelViewSet
from ..serializers.client_document import ClientDocumentModelSerializer
from wabot.base.authentication import TokenAPIAuthentication


class ClientDocumentView(BaseModelViewSet):
    """
        create:
            <p>Cria novo cadastro do Documento do CLiente.<p>
            <b>Funcionalidades:</b>
            <p>&ensp;&ensp;Receber arquivo no formato png;<p>
            <p>&ensp;&ensp;Salvar informações na base de dados;<p>

        retrieve:
            Retorna documento filtrando pelo código.

        update:
            Atualizar Documento.
            <n>
            <b>Parâmetros:</b>
            <b>&ensp;&ensp;id:</b> código referente Documento.
            <b>&ensp;&ensp;data:</b> json para atualização das informações.

        partial_update:
            Atualizar um ou mais campos em um Documento.
            <n>
            <b>Parâmetros:</b>
            <b>&ensp;&ensp;id:</b> código referente ao Documento.
            <b>&ensp;&ensp;data:</b> json para atualização das informações.

        delete:
            Excluir Documento.
            <n>
            <b>Parâmetro:</b>
            <b>&ensp;&ensp;id:</b> código referente ao Documento.

        relationship:
            Verifica se o registro possui vínculo com outro.
        """
    serializer_class = ClientDocumentModelSerializer
    parser_classes = [MultiPartParser]
    my_tags = ['Documento Cliente']
    authentication_classes = [TokenAPIAuthentication]
    permission_classes = [IsAuthenticated, AllowAny]

    class Meta:
        model = ClientDocumentModelSerializer.Meta.model
