from owner import models
from rest_framework import serializers

class LibrarySerializer(serializers.Serializer):
    class Meta:
        model = models.Library
        fields = '__all__'
