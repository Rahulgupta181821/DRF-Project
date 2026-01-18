from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlateform
class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"
    
    
class StreamPlateformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True,read_only = True)
    class Meta:
        model = StreamPlateform
        fields = "__all__"