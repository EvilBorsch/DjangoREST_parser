from django.db import models

from .serializers import SearchQuerySerializer, MessageSerializer
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
    def get_messages(company_guid, searching_by):
        parser = Parser()
        messages_raw = parser.get_messages(company_guid)

        messages = list()
        for raw_message in messages_raw:

            message_type = raw_message["type"]
            if (message_type != "BankruptcyMessage"):
                continue

            is_fraze_in = parser.is_text_in(searching_by, str(raw_message))

            if searching_by != "" and not (searching_by != "" and is_fraze_in):
                continue

            url = "https://bankrot.fedresurs.ru/MessageWindow.aspx?ID={}".format(raw_message["guid"])
            message = Message(company_guid=company_guid, message_guid=raw_message["guid"], type=message_type,
                              datePublish=raw_message["datePublish"], text=raw_message["title"], url=url)
            messages.append(message)
            message.save()

        return messages

    def __str__(self):
        return self.name


class Message(models.Model):
    company_guid = models.CharField(max_length=200, db_index=True)
    message_guid = models.CharField(max_length=200, primary_key=True)
    type = models.CharField(max_length=100, default='BankruptcyMessage')
    datePublish = models.DateTimeField()
    text = models.TextField()
    url = models.TextField()

    @staticmethod
    def serialize(messages):
        return MessageSerializer(messages, many=True).data

    @staticmethod
    def get_messages_from_db(company_guid, searching_by):
        messages = Message.objects.filter(company_guid=company_guid, text__contains=searching_by)
        return Message.serialize(messages)

    def __str__(self):
        return self.text


class SearchQuery(models.Model):
    searchText = models.CharField(max_length=200, primary_key=True)
    company_guid = models.CharField(max_length=200)

    def __str__(self):
        return self.searchText

    @staticmethod
    def get_by_search_text(searchText):
        querys = SearchQuery.objects.filter(searchText=searchText)
        serializedData = SearchQuerySerializer(querys, many=True).data
        return serializedData

    def serialize_and_save(self):
        self.save()
        return SearchQuerySerializer(self).data

    @staticmethod
    def get_companys_by_search_text(company_name):
        parser = Parser()
        companys = parser.get_companys_list_by_name(company_name)
        return companys
