from rest_framework import serializers


class SearchQuerySerializer(serializers.Serializer):
    searchText = serializers.CharField(max_length=200)
    guid = serializers.CharField(max_length=200)
