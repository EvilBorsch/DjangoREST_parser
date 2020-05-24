from django.urls import path

from .views import GetSearchGUIDView, GetMessagesByGUIDView

app_name = "proj"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('get', GetSearchGUIDView.as_view()),
    path('get_messages',GetMessagesByGUIDView.as_view())
]
