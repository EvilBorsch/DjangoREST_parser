# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SearchQuery


class GetSearchGUIDView(APIView):
    def get(self, request):
        company_name = request.data["company_name"]
        guid = SearchQuery.get_guid_by_search_text(company_name)
        query = SearchQuery(company_name, guid)
        return Response(query.serializeAndSave())

    def post(self, request):
        data = request.data["searchText"]
