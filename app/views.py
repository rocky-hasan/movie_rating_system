from django.shortcuts import render
from .serializers import MovieSerializer,RatingSerializer
from .models import Movie,Rating
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
# Create your views here.


class MovieSerializerView(viewsets.ModelViewSet):
    qryset=Movie.objects.all()
    serializer_class=MovieSerializer


class RatingSerializerView(viewsets.ModelViewSet):
    qryset=Rating.objects.all()
    serializer_class=RatingSerializer

class Moviesearch(APIView):
    def get(self,request):
        queryset=request.GET.get('query','')
        movie=get_object_or_404(Movie,name__icontains=queryset)
        ratings=Rating.objects.filter(movie=movie)
        total_ratings = len(ratings)
        if total_ratings > 0:
            average_rating = sum([rating.rating for rating in ratings]) / total_ratings
        else:
            average_rating = 0 
        serializer = MovieSerializer(movie)
        context_data={
            'movie_details': serializer.data,
            'average_rating': average_rating
        }
        return JsonResponse(context_data)