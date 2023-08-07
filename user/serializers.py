from rest_framework import serializers
from .models import *
from helper import choice_keys

class UserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm
        fields = '__all__'

class AllUserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm
        fields = ['name','contact_no']

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recipient = serializers.EmailField()
    attachment = serializers.FileField(required=False)

class RequestAdminViewSerializer(serializers.Serializer):
    name = serializers.CharField()
    choice = serializers.ChoiceField(choices=choice_keys.REQUEST_ACCESS_CHOICES)
    data = serializers.CharField()