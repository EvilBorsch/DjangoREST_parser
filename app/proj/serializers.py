from rest_framework import serializers


class SearchQuerySerializer(serializers.Serializer):
    searchText = serializers.CharField(max_length=200)
    company_guid = serializers.CharField(max_length=200)


class MessageSerializer(serializers.Serializer):
    company_guid = serializers.CharField(max_length=200)
    message_guid = serializers.CharField(max_length=200)
    type = serializers.CharField(max_length=100)
    datePublish = serializers.DateTimeField()
    text = serializers.CharField()
    url = serializers.CharField()
