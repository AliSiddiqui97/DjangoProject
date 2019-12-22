from .models import Destination
from rest_framework import viewsets, permissions
from .serializers import DestinationSerializer


class DestinationViewSet(viewsets.ModelViewSet):
    queryset=Destination.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DestinationSerializer
