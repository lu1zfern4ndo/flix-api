from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import MovieSerializer


class MovieCreateList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDetroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
