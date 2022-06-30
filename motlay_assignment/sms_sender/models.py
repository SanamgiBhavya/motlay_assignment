from django.db import models
from uuid import uuid4
from sms_sender.constants.enums import SMSProvider, SMSStatus
from simple_history.models import HistoricalRecords


class SMSProviderConfig(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    sms_provider = models.CharField(max_length=50, choices=SMSProvider.get_list_of_tuples())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    throughput = models.IntegerField()
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords(
        history_change_reason_field=models.TextField(null=True))

    def __str__(self):
        return "%s %s" % (str(self.sms_provider), self.throughput)


class SMSStatusDetails(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    sms_provider = models.ForeignKey(SMSProviderConfig, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=SMSStatus.get_list_of_tuples())
    retrigger_count = models.IntegerField(default=1)
    history = HistoricalRecords(
        history_change_reason_field=models.TextField(null=True))

    def __str__(self):
        return "%s %s" % (str(self.id), self.status)