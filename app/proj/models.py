from django.db import models

from .serializers import SearchQuerySerializer
from .utils.parser.parser import Parser





class Company(models.Model):
    guid = models.CharField(max_length=200, primary_key=True)
    ogrn = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    address = models.TextField()
    status = models.TextField()
    status_date = models.DateTimeField()

    @staticmethod
    def get_messages(company_guid):
        parser=Parser()
        messages=parser.get_messages(company_guid)




    def __str__(self):
        return self.name


class SearchQuery(models.Model):
    searchText = models.CharField(max_length=200, primary_key=True)
    guid = models.CharField(max_length=200)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True)

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
    def get_companys_by_search_text(company_name):
        parser = Parser()
        companys = parser.get_companys_list_by_name(company_name)
        return companys

