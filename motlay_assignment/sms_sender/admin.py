from django.contrib import admin
from sms_sender.models import SMSProviderConfig, SMSStatusDetails
# Register your models here.


admin.site.register(SMSProviderConfig)
admin.site.register(SMSStatusDetails)