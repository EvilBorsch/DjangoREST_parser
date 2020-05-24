from django.db import models

from .serializers import SearchQuerySerializer
from .utils.parser.parser import Parser


class SearchQuery(models.Model):
    searchText = models.CharField(max_length=200, primary_key=True)
    guid = models.CharField(max_length=200)

    def __str__(self):
        return self.searchText

    @staticmethod
    def getAll():
        querys = SearchQuery.objects.all()
        serializedData = SearchQuerySerializer(querys, many=True).data
        return serializedData

    @staticmethod
    def getBySearchText(text):
        querys = SearchQuery.objects.filter(searchText=text)
        serializedData = SearchQuerySerializer(querys, many=True).data

        return serializedData

    def serializeAndSave(self):
        self.save()
        return SearchQuerySerializer(self).data

    @staticmethod
    def get_guid_by_search_text(company_name):
        parser = Parser()
        guid = parser.get_guid(company_name)
        return guid
