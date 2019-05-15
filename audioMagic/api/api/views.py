from rest_framework import viewsets

from .serializers import MagicSerializers

from ..models import Magic

class MagicView(viewsets.ModelViewSet):
    queryset = Magic.objects.all()
    serializer_class = MagicSerializers