from django.db import models

# Create your models here.
class Library(models.Model):
    lib_name = models.CharField(max_length=500,null=True, blank=True)     
    lib_address = models.TextField(null=True, blank=True)
    lib_contact = models.CharField(max_length=10, null=True, blank=True)
