from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Genre
from .serializers import GenreSerializer


class GenreCreateList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
