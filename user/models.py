from django.db import models
from helper.validators import *


class UserForm(models.Model):
    name = models.CharField(max_length=500,null=True, blank=True)
    photo=models.FileField(upload_to='uploads/photo/',  null=True, blank=True)
    email = models.EmailField(unique=True,null=True, blank=True)
    contact_no=models.CharField(max_length= 10 ,unique=True, validators = [mobile_regex], error_messages={"unique": "Mobile number is already registered"},null=True, blank=True)
    gurdian_mobile_no = models.CharField(max_length=10, null=True, blank=True, validators = [mobile_regex])
    id_proof = models.FileField(upload_to='uploads/id_proof/',  null=True, blank=True)
    fathers_name = models.CharField(max_length=500,null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    preparation_course = models.CharField(max_length=500,null=True, blank=True)
    current_address = models.TextField(null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)
    district = models.CharField(max_length=500,null=True, blank=True)
    pincode = models.CharField(max_length=6 , null=True, blank=True)
    state = models.CharField(max_length=500,null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True, blank=True)
    timing_hrs = models.IntegerField(null=True, blank=True)
    seat_no = models.IntegerField(null=True, blank=True)
    session = models.IntegerField(null=True, blank=True)
    want_copy = models.BooleanField(null=True, blank=True)
    form_copy = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    
