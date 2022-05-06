import logging

from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from django.conf import settings

LOG = logging.getLogger(__name__)


def get_swagger_redoc_header(request):
    http_referer = request.META.get('PATH_INFO')
    return 'swagger' in http_referer or 'redoc' in http_referer


class TokenAPIAuthentication(BaseAuthentication):
    keyword = 'Token'

    def authenticate(self, request):
        # Allow if request is from swagger or redoc
        if get_swagger_redoc_header(request):  # pragma: no cover
            return User(), None
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:  # pragma: no cover
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(request, token)

    def authenticate_credentials(self, request, token):
        if not token == str(settings.API_SECRET_KEY):
            msg = _('Invalid token.')
            raise exceptions.AuthenticationFailed(msg)
        return User(), token
