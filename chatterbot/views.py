from django.conf import settings
from django.http import HttpResponse


def index(request):
    return HttpResponse(f'Ciências da Computação - Chatter Bot\n'
                        f'Versão:{settings.BUILD_VERSION}')
