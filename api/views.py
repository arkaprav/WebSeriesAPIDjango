from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

# Create your views here.

class StreamPlatformListAV(APIView):

    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class SingleStreamPlatformAV(APIView):

    def get(self, request, pk):
        platform = StreamPlatform.objects.get(pk = pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk = pk)
        serializer = StreamPlatformSerializer(platform, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk = pk)
        platform.delete()
        return Response({"message": "The particular platform has been deleted!!!"})


class WebSeriesListAV(APIView):

    def get(self, request):
        WebSerieslist = WebSeries.objects.all()
        serializer = WebSeriesSerializer(WebSerieslist, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WebSeriesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class SingleWebSeriesAV(APIView):

    def get(self, request, pk):
        webseries = WebSeries.objects.get(pk = pk)
        serializer = WebSeriesSerializer(webseries)
        return Response(serializer.data)
    
    def put(self, request, pk):
        webseries = WebSeries.objects.get(pk = pk)
        serializer = WebSeriesSerializer(webseries, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        webseries = StreamPlatform.objects.get(pk = pk)
        webseries.delete()
        return Response({"message": "The particular WebSeries has been deleted!!!"})
    

class ReviewListAV(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(webseries=pk)
    
class ReviewCreateAV(generics.CreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        webseries = WebSeries.objects.get(pk=pk)
        serializer.save(webseries=webseries)
    

class SingleReviewAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer