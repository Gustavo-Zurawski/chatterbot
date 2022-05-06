from django.conf import global_settings, settings
from django.core.files.storage import get_storage_class
from storages.backends.s3boto3 import S3Boto3Storage

DefaultMediaSotare = get_storage_class(global_settings.DEFAULT_FILE_STORAGE)
secure_storage = DefaultMediaSotare()

if settings.USE_S3:
    common_params = {
        'secure_urls': True,
        'headers': {
            'Cache-Control': 'max-age=604800',
        },
    }

    public_params = {
        'querystring_auth': False,
        'acl': 'public-read',
    }
    public_params.update(common_params)

    private_params = {
        'querystring_auth': True,
        'acl': 'private',
        'querystring_expire': 60 * 10,
    }
    private_params.update(common_params)


    class SecureStorage(S3Boto3Storage):
        def __init__(self, *args, **kwargs):
            params = {
                'bucket': settings.AWS_S3_SECURE_BUCKET,
                'location': settings.AWS_S3_ENVIRONMENT,
            }
            private_params['access_key'] = settings.AWS_S3_ACCESS_KEY_ID
            private_params['secret_key'] = settings.AWS_S3_SECRET_ACCESS_KEY
            params.update(private_params)
            params.update(kwargs)
            super(SecureStorage, self).__init__(*args, **params)

        def path(self, name):
            return self._normalize_name(name)

    secure_storage = SecureStorage()
