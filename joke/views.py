from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import action
import random
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from joke.models import Joke
from joke.serializer import JokeSerializer


class JokeViewSet(ModelViewSet):

    serializer_class = JokeSerializer
    permission_classes = (AllowAny, )
    queryset = Joke.objects.all()

    @action(detail=False, methods=['get'])
    def stats(self, request):
        stats = {
            'count': Joke.objects.count()
        }
        return Response(data=stats, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def random(self, request):
        queryset = self.get_queryset()
        count = queryset.count()
        random_value = random.randrange(0, count)
        joke = queryset[random_value]
        serializer = JokeSerializer(instance=joke)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
