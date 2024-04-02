from django.shortcuts import render
from .serializers import MovieSerializer,RatingSerializer
from .models import Movie,Rating
from rest_framework import viewsets
# Create your views here.


class MovieSerializerView(viewsets.ModelViewSet):
    qryset=Movie.objects.all()
    serializer_class=MovieSerializer


class RatingSerializerView(viewsets.ModelViewSet):
    qryset=Rating.objects.all()
    serializer_class=RatingSerializer
