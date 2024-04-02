
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MovieSerializerView,RatingSerializerView

router=DefaultRouter()
router.register(r'movies',MovieSerializerView, basename='movie')
router.register(r'ratings',RatingSerializerView, basename='rating')

urlpatterns = [
    path('', include(router.urls)),
]