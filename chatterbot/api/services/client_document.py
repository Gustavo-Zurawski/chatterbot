import logging
import boto3
import re
import face_recognition
import numpy

from io import BytesIO
from django.conf import settings
from chatterbot.base.service import ModelServiceMixin
from ..models import Client


LOG = logging.getLogger(__name__)


class ClientDocumentModelService(ModelServiceMixin):
    model = Client

    @classmethod
    def get_numbers(cls, value: str):
        return ''.join(re.findall(r'\d', str(value)))

    @classmethod
    def process_data_by_document(cls, documento):
        try:
            client = Client()
            client = cls.get_document_data(documento.name, client)
            client = cls.processed_face_recognition(documento, client)
            client.document = documento
            client.save()
        except Exception as error:
            LOG.error(f'[SAVE_DOCUMENT] document: {documento} error: {error}')

    @classmethod
    def get_document_data(cls, file_name, client: Client):
        rekognition = boto3.client('rekognition')

        response = rekognition.detect_text(Image={'S3Object': {'Bucket': settings.AWS_S3_SECURE_BUCKET,
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
                client.name = str(text['DetectedText']).title()
            if text['Id'] == 12:
                client.cpf = cls.get_numbers(str(text['DetectedText']))
            if text['Id'] == 8:
                client.rg = cls.get_numbers(str(text['DetectedText']))

        return client

    @classmethod
    def processed_face_recognition(cls, document, client: Client):
        photo = document.photo.read()
        imagem = face_recognition.load_image_file(BytesIO(photo))
        face_encoding = face_recognition.face_encodings(face_image=imagem)
        string = str(face_encoding[0]).replace('[', '').replace(']', '').replace('\n', '')
        client.face_coding = string
        return client

    @classmethod
    def get_client_by_image(cls, image):
        try:
            image = face_recognition.load_image_file(BytesIO(image))
            if face_recognition.face_locations(img=image):
                encoding_check = face_recognition.face_encodings(face_image=image)
                client_id = cls.checked_images(encoding_check)
                return cls.get_all().filter(id=client_id).first()
        except Exception as error:
            LOG.error(f'[GET_CLIENT_BY_IMAGE] error: {error}')
            raise NameError(error)

    @classmethod
    def get_client_data_face_encoding(cls):
        clietns = cls.get_all().filter(face_coding__isnull=False).all()
        image_list = []
        id_list = []
        for client in clietns:
            image_string = client.face_coding.decode()
            face_encoding = numpy.fromstring(string=image_string, dtype=numpy.float, sep=' ')
            image_list.append(face_encoding)
            id_list.append(client.id)
        return image_list, id_list

    @classmethod
    def checked_images(cls, encoding_check):
        try:
            encodings, ids = cls.get_client_data_face_encoding()
            result = face_recognition.compare_faces(known_face_encodings=encodings,
                                                    face_encoding_to_check=encoding_check[0],
                                                    tolerance=0.4)

            position = 0
            for matche in result:
                if matche:
                    return ids[position]
                position += 1
        except Exception as error:
            LOG.error(f'[CHECKED_IMAGES] error: {error}')
            raise NameError(error)
