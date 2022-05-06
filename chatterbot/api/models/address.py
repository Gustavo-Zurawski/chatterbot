from django.db import models
from chatterbot.base.models import BaseModel


class Address(BaseModel):
    client = models.ForeignKey('api.Client', on_delete=models.CASCADE)
    cep = models.CharField(max_length=15)
    street = models.CharField(max_length=100)
    number = models.IntegerField(default=None, blank=True, null=True)
    district = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        db_table = 'address'
