from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlateform
class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"
    
    
class StreamPlateformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True,read_only = True)
    # watchlist = serializers.StringRelatedField(many=True)
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-detail'
    )

    class Meta:
        model = StreamPlateform
        fields = "__all__"
