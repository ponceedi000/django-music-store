from rest_framework import generics
from .serializer import MusicSerializer
from .models import Music

class MusicList(generics.ListAPIView):
  queryset = Music.objects.all()
  serializer_class = MusicSerializer

class MusicDetail(generics.RetrieveAPIView):
  queryset = Music.objects.all()
  serializer_class = MusicSerializer