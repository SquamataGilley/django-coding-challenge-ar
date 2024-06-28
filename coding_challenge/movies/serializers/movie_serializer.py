from rest_framework import serializers
from movies.models.movie import Movie
from movies.models.review import Review

class MovieSerializer(serializers.ModelSerializer):
    runtime_formatted = serializers.SerializerMethodField()
    reviewers = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'runtime', 'runtime_formatted', 'reviewers', 'avg_rating']

    def get_runtime_formatted(self, obj):
        hours = obj.runtime // 60
        minutes = obj.runtime % 60
        return f"{hours}:{minutes:02d}"

    def get_reviewers(self, obj):
        reviews = Review.objects.filter(movie=obj)
        return [{'name': review.reviewer_name, 'rating': review.rating} for review in reviews]

    def get_avg_rating(self, obj):
        reviews = Review.objects.filter(movie=obj)
        if reviews.exists():
            total_ratings = sum([review.rating for review in reviews])
            avg_rating = total_ratings / len(reviews)
            return round(avg_rating, 2)
        else:
            return None
