# Generated by Django 3.2.8 on 2022-05-06 01:33

import wabot.base.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created')),
                ('id', models.AutoField(db_column='id_document', primary_key=True, serialize=False)),
                ('file', models.FileField(storage=wabot.base.storage.SecureStorage(), upload_to='')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
                'db_table': 'document',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created')),
                ('name', models.CharField(max_length=200)),
                ('rg', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('issuing_body', models.CharField(blank=True, default=None, max_length=8, null=True)),
                ('uf', models.CharField(blank=True, default=None, max_length=3, null=True)),
                ('cpf', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('birth_date', models.DateField(blank=True, default=None, null=True)),
                ('local', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('issuance_date', models.DateField(blank=True, default=None, null=True)),
                ('face_coding', models.TextField(blank=True, default=None, null=True)),
                ('photo', models.FileField(blank=True, default=None, null=True, upload_to='', verbose_name=wabot.base.storage.SecureStorage())),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.document')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created')),
                ('cep', models.CharField(max_length=15)),
                ('street', models.CharField(max_length=100)),
                ('number', models.IntegerField(blank=True, default=None, null=True)),
                ('district', models.CharField(max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.client')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
                'db_table': 'address',
            },
        ),
    ]
