from rest_framework import serializers
from movies.models.review import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'reviewer_name', 'rating']
        read_only_fields = ['movie']
