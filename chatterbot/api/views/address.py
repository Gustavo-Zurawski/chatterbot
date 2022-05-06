from rest_framework.permissions import AllowAny, IsAuthenticated

from chatterbot.base.api_view import BaseModelViewSet
from ..serializers.address import AddressModelSerializer
from chatterbot.base.authentication import TokenAPIAuthentication


class AddressView(BaseModelViewSet):
    """
        create:
            <p>Cria novo cadastro do Endereço.<p>
            <b>Funcionalidades:</b>
            <p>&ensp;&ensp;Receber Endereço do cliente;<p>
            <p>&ensp;&ensp;Salvar informações na base de dados;<p>

        retrieve:
            Retorna endereço filtrando pelo código.

        update:
            Atualizar Endereço.
            <n>
            <b>Parâmetros:</b>
            <b>&ensp;&ensp;id:</b> código referente Endereço.
            <b>&ensp;&ensp;data:</b> json para atualização das informações.

        partial_update:
            Atualizar um ou mais campos em um Endereço.
            <n>
            <b>Parâmetros:</b>
            <b>&ensp;&ensp;id:</b> código referente ao Endereço.
            <b>&ensp;&ensp;data:</b> json para atualização das informações.

        delete:
            Excluir Endereço.
            <n>
            <b>Parâmetro:</b>
            <b>&ensp;&ensp;id:</b> código referente ao Endereço.

        relationship:
            Verifica se o registro possui vínculo com outro.
        """
    serializer_class = AddressModelSerializer
    my_tags = ['Endereço']
    authentication_classes = [TokenAPIAuthentication]
    permission_classes = [IsAuthenticated, AllowAny]

    class Meta:
        model = AddressModelSerializer.Meta.model
