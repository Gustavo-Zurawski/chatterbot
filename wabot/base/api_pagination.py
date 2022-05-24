from collections import OrderedDict
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
import os


class LimitOffsetPaginationMixin(LimitOffsetPagination):
    def get_paginated_response(self, data):
        headers = {
            'X-BUILD_VERSION': os.getenv('BUILD_VERSION', 'Not Found')
        }
        return Response(OrderedDict([
            ('count', self.get_count(data)),
            ('total', self.count),
            ('limit', self.limit),
            ('offset', self.offset),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]), headers=headers)

    @staticmethod
    def get_paginated_response_minha_conta(data, limit, offset, status):
        headers = {
            'X-BUILD_VERSION': os.getenv('BUILD_VERSION', 'Not Found')
        }
        return Response(OrderedDict([
            ('count', len(data['results'])),
            ('total', data['count']),
            ('limit', limit),
            ('offset', offset),
            ('next', data['next']),
            ('previous', data['previous']),
            ('results', data['results'])
        ]), headers=headers, status=status)
