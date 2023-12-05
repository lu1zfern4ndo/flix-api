from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Actor
from .serializers import ActorSerializer


class ActorCreateList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
