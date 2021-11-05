""" Configure location of static and media files for s3 bucket """
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    """ Configure location of static files for s3 bucket """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ Configure location of media files for s3 bucket """
    location = settings.MEDIAFILES_LOCATION
