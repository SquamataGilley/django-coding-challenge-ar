from rest_framework import generics

from movies.models.movie import Movie
from movies.serializers.movie_serializer import MovieSerializer

class MovieListView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
            #
        runtime = self.request.query_params.get('runtime')
        choice = self.request.query_params.get('choice')

        if runtime and choice:
            if choice == 'shorter':
                queryset = queryset.filter(runtime__lt=runtime)
            elif choice == 'longer':
                queryset = queryset.filter(runtime__gte=runtime)

        return queryset
