from django.db import models
from chatterbot.base.models import BaseModel
from chatterbot.base.storage import secure_storage


class Document(BaseModel):
    id = models.AutoField(primary_key=True, db_column='id_document')
    file = models.FileField(storage=secure_storage)
    name = models.CharField(max_length=100, null=True, blank=True, default=None)
    photo = models.FileField(storage=secure_storage, null=True, blank=True, default=None)

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        db_table = 'document'
