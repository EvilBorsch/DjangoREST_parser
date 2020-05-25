from django.contrib import admin

# Register your models here.
from .models import SearchQuery, Company, Message

admin.site.register(SearchQuery)
admin.site.register(Company)
admin.site.register(Message)
