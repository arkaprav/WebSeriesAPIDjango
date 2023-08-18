from rest_framework import serializers
from .models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('watch',)
        # fields = "__all__"

class WebSeriesSerializer(serializers.ModelSerializer):
    # review = serializers.StringRelatedField(many=True, read_only=True)
    review = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WebSeries
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):

    # WebSerieslist = WebSeriesSerializer(many=True, read_only=True)
    webseries = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"