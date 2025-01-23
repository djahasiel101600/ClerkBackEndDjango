from rest_framework import serializers
from .models import IARRecord, PORecord

class IARSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IARRecord
        fields = '__all__'

    
class POSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PORecord
        fields = '__all__'