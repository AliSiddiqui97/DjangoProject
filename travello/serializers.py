from rest_framework import serializers
from .models import Destination 

# Lead Serializer
class DestinationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Destination 
    fields = '__all__'
