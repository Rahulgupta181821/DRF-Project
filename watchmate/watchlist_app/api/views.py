from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from watchlist_app.models import WatchList,StreamPlateform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlateformSerializer, ReviewSerializer

class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ReviewList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    

class StreamPlateformAV(APIView):
    def get(self, request):
        stream_plateform = StreamPlateform.objects.all()
        serializer = StreamPlateformSerializer(stream_plateform, many = True, context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StreamPlateformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlateformDetailAV(APIView):
    def get(self,request, pk):
        try:
            stream_plateform = StreamPlateform.objects.get(pk=pk)
        except StreamPlateform.DoesNotExist:
            return Response({'error': 'Not Found'},status = status.HTTP_404_NOT_FOUND)
        serializer= StreamPlateformSerializer(stream_plateform,context={'request': request})
        return Response(serializer.data)
    
    def put(self,request,pk):
        plateform = StreamPlateform.objects.get(pk=pk)
        serializer = StreamPlateformSerializer(plateform, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request, pk):
        plateform = StreamPlateform.objects.get(pk=pk)
        plateform.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchDetailAV(APIView):
    def get(self, request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Not Found.'},status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

