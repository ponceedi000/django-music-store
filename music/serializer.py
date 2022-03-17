from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'seller', 'name', 'instrument', 'description', 'created_at', 'updated_at')
    model = Music