from rest_framework import serializers
from .models import IARRecord

class IARSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IARRecord
        fields = '__all__'