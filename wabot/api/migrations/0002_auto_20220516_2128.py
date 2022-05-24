# Generated by Django 3.2.8 on 2022-05-17 00:28

import wabot.base.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='photo',
            field=models.FileField(blank=True, default=None, null=True, storage=wabot.base.storage.SecureStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='client',
            name='rg',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]