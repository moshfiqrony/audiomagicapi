from rest_framework import serializers

from ..models import Magic

class MagicSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Magic
        fields = ('id', 'name', 'audioFile')