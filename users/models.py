from django.db import models
import time
from django.core.validators import RegexValidator

import random
from random import randint

owner = models.ForeignKey('auth.User', related_name='register')
highlighted = models.TextField()

# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
# fs = FileSystemStorage(location=settings.STATIC_ROOT)

class Users(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True,default='')
    email = models.EmailField(max_length=100, blank=True,default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Enter country code. Phone number must be entered in the format: '919999999'.")
    phone = models.CharField(max_length=12,validators=[phone_regex], blank=True) # validators should be a list
    project_description = models.CharField(max_length=100, blank=True,default='')
    domain = models.CharField(max_length=100, blank=True,default='')
    

   # photo = models.ImageField(upload_to="projectimg/",storage=fs, null=True, blank=True)
    
    
    class Meta:
        ordering = ('created',)
