from django.db import models
from chatterbot.base.models import BaseModel
from chatterbot.base.storage import secure_storage


class Client(BaseModel):
    name = models.CharField(max_length=200)
    rg = models.CharField(max_length=30, default=None, null=True, blank=True)
    issuing_body = models.CharField(max_length=8, default=None, null=True, blank=True)
    uf = models.CharField(max_length=3, default=None, null=True, blank=True)
    cpf = models.CharField(max_length=20, default=None, null=True, blank=True)
    birth_date = models.DateField(default=None, null=True, blank=True)
    local = models.CharField(max_length=20, default=None, null=True, blank=True)
    issuance_date = models.DateField(default=None, null=True, blank=True)
    face_coding = models.TextField(default=None, null=True, blank=True)
    document = models.ForeignKey('api.Document', on_delete=models.CASCADE)
    photo = models.FileField(secure_storage, default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'client'
