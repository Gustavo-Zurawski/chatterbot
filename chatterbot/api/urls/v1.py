from rest_framework.routers import DefaultRouter

from ..views.client import ClientView, ClientFaceRecognitionView
from ..views.client_document import ClientDocumentView
from ..views.address import AddressView

router = DefaultRouter(trailing_slash=False)
router.register(r'client', ClientView, 'client')
router.register(r'client-document', ClientDocumentView, 'client-document')
router.register(r'client-face-recognition', ClientFaceRecognitionView, 'client-face-recognition')
router.register(r'address', AddressView, 'address')
