from rest_framework import mixins
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import GenericViewSet


class BaseViewSet(GenericViewSet):
    filter_backends = [OrderingFilter]
    filterset_fields = '_all_'
    ordering_fields = '_all_'
    permission_functionality = None

    @property
    def model(self):
        if not (meta := getattr(self.serializer_class, 'Meta', None)):
            meta = getattr(self, 'Meta', None)
        assert meta, (
            "'%s' or its serializer should either include a `Meta` class, "
            'or override the `model` view attribute.' % self._class.name_
        )
        return meta.model

    def list(self, request, *args, **kwargs):
        # Swagger documentation
        """
        Retorna todos os registros.
        <n>
        Esse método utiliza controle por paginação.
        <p>Parâmetro <b><i>limit</i></b> possuí valor <i><b>default=100</b></i>,
        usado para limitar a quantidade de registros por página.<p>
        <p>Parâmetro <b><i>offset</i></b> possuí valor <i><b>default=0</b></i>,
        controla o deslocamento de página.</p>
        <p><b>Obs.:</b> Os demais campos são utilizados para filtrar dados.</p>
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def get_queryset(self):
        if self.detail and hasattr(self.model.objects, 'with_deleted'):
            return self.model.objects.with_deleted()
        return self.model.objects.all()


class BaseModelViewSet(
    BaseViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
):
    pass


class BaseModelReadOnlyViewSet(BaseViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    pass
