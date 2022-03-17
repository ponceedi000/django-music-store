from rest_framework import generics
from .serializer import MusicSerializer
from .models import Music

class MusicList(generics.ListCreateAPIView):
  queryset = Music.objects.all()
  serializer_class = MusicSerializer

class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Music.objects.all()
  serializer_class = MusicSerializer