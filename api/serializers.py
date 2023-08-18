from rest_framework import serializers
from .models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('webseries',)

class WebSeriesSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WebSeries
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    webseries = WebSeriesSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"