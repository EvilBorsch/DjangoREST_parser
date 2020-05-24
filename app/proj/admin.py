from django.contrib import admin

# Register your models here.
from .models import SearchQuery, Company

admin.site.register(SearchQuery)
admin.site.register(Company)
