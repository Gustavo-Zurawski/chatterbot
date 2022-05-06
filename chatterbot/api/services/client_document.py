import logging
import boto3

from django.conf import settings
from chatterbot.base.service import ModelServiceMixin
from ..models import Client


LOG = logging.getLogger(__name__)


class ClientDocumentModelService(ModelServiceMixin):
    model = Client

    @classmethod
    def process_data_by_document(cls, documento):
        try:
            name = cls.get_document_data(documento.name)
            client = Client()
            client.document = documento
            client.name = name
            client.save()
        except Exception as error:
            LOG.error(f'[SAVE_DOCUMENT] document: {documento} error: {error}')

    @classmethod
    def get_document_data(cls, file_name):
        client = boto3.client('rekognition')

        response = client.detect_text(Image={'S3Object': {'Bucket': settings.AWS_S3_SECURE_BUCKET,
                                                          'Name': file_name}})

        textDetections = response['TextDetections']
        print('Detected text\n----------')

        for text in textDetections:
            print('Detected text:' + text['DetectedText'])
            print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print('Parent Id: {}'.format(text['ParentId']))
            print('Type:' + text['Type'])
            print()
            if text['Id'] == 6:
                resutl = str(text['DetectedText']).title()
                return resutl
