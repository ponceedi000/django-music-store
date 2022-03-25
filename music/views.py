from rest_framework import generics
from .serializer import MusicSerializer
from .models import Music
from .permissions import isOwnerOrReadOnly

class MusicList(generics.ListCreateAPIView):
  permission_classes = (isOwnerOrReadOnly,)
  queryset = Music.objects.all()
  serializer_class = MusicSerializer

class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (isOwnerOrReadOnly,)
  queryset = Music.objects.all()
  serializer_class = MusicSerializer