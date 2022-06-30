from django.urls import path
from sms_sender.views import SendSMSView


urlpatterns = [
    path('send_sms/v1/', SendSMSView.as_view(), name='send_sms')
]