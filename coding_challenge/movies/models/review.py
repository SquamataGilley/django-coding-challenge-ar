from django.db import models
from movies.models.movie import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.reviewer_name} - {self.rating}/5"
