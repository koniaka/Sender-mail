from django.urls import path
from mail_sender.views import ListMail, CreateMail

app_name = 'sender'
urlpatterns = [
    path('', CreateMail.as_view(), name='form'),
    path('list/', ListMail.as_view(), name='mail_list'),
]