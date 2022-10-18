import os
import magic
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_billFile_type(upload):
    # Make uploaded file accessible for analysis by saving in tmp
    tmp_path = 'tmp/%s' % upload.name[2:]
    default_storage.save(tmp_path, ContentFile(upload.file.read()))
    full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)
    print(full_tmp_path )
    # Get MIME type of file using python-magic and then delete
    file_type = magic.from_file(full_tmp_path, mime=True)
    print(file_type)
    default_storage.delete(tmp_path)

    # Raise validation error if uploaded file is not an acceptable form of media
    extension = full_tmp_path.split(".")[-1]
    print(extension == "xlsx")
    if file_type not in settings.BILL_FILE_TYPES and extension != "xlsx":
        print("error")
        raise ValidationError('File type not supported. JPEG, PNG, or xlsx recommended')

def validate_image_type(upload):
    tmp_path = 'tmp/%s' % upload.name[2:]
    default_storage.save(tmp_path, ContentFile(upload.file.read()))
    full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)
    file_type = magic.from_file(full_tmp_path, mime=True)
    default_storage.delete(tmp_path)
    print(file_type)
    if file_type not in settings.IMAGE_TYPES:
        raise ValidationError(_('File type not supported. JPEG, PNG recommended'))
   
def validate_file_type(upload):
    tmp_path = 'tmp/%s' % upload.name[2:]
    default_storage.save(tmp_path, ContentFile(upload.file.read()))
    full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)
    file_type = magic.from_file(full_tmp_path, mime=True)
    default_storage.delete(tmp_path)
    print(file_type)
    if file_type not in settings.FILE_TYPES:
        raise ValidationError(_('File type not supported. JPEG, PNG, or pdf recommended'))

def validate_products_file_type(upload):
    tmp_path = 'tmp/%s' % upload.name[2:]
    default_storage.save(tmp_path, ContentFile(upload.file.read()))
    full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)
    file_type = magic.from_file(full_tmp_path, mime=True)
    default_storage.delete(tmp_path)
    extension = full_tmp_path.split(".")[-1]
    print(file_type)
    if extension != "xlsx":
        raise ValidationError(_('File type not supported. xlsx recommended'))
