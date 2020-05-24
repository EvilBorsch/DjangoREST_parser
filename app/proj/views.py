# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SearchQuery, Company


class GetSearchGUIDView(APIView):
    def get(self, request):
        company_name = request.data["company_name"]
        """
         because we looking only for 
         first company(i can parse all if u want)
        """
        company_raw = SearchQuery.get_companys_by_search_text(company_name)[0]

        company = Company(company_raw["guid"], company_raw["ogrn"], company_raw["inn"], company_raw["name"],
                          company_raw["address"], company_raw["status"],
                          company_raw["statusDate"])
        guid = company.guid
        company.save()
        query = SearchQuery(company_name, guid, company)
        return Response(query.serializeAndSave())

    def post(self, request):
        data = request.data["searchText"]