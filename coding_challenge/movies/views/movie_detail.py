from rest_framework import generics

from movies.models.movie import Movie
from movies.serializers.movie_serializer import MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'
