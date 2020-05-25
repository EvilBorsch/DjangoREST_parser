# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SearchQuery, Company, Message


class GetSearchGUIDView(APIView):
    def get(self, request):
        company_name = request.data["company_name"]

        """
         because we looking only for first company in list i add only first
         first company(i can parse all if u want)
        """

        # query = SearchQuery.get_by_search_text(company_name)  # get from db
        # if (query == []):
        
        # get Guid form fedres site
        raw_companys_list = SearchQuery.get_companys_by_search_text(company_name)
        if (raw_companys_list == []):
            return Response([])
        company_raw = raw_companys_list[0]
        company = Company(company_raw["guid"], company_raw["ogrn"], company_raw["inn"], company_raw["name"],
                          company_raw["address"], company_raw["status"],
                          company_raw["statusDate"])
        company.save()
        query = SearchQuery(company_name, company.guid)
        return Response([query.serialize_and_save()])
        # return Response(query)


class GetMessagesByGUIDView(APIView):
    def get(self, request):
        company_guid = request.data["company_guid"]
        searching_by = request.data["searching_by"]
        # messages = Message.get_messages_from_db(company_guid, searching_by) # get messages from db

        # Get messages from fedres site
        messages = Company.get_messages(company_guid, searching_by)

        return Response(Message.serialize(messages))
