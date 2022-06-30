import typing

from sms_sender.interactors.dtos import SMSStatusDetailsDTO
from sms_sender.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from sms_sender.exceptions import custom_exceptions
from sms_sender.models import *
from sms_sender.interactors.storage_interfaces import dtos as storage_dtos


class StorageImplementation(StorageInterface):

    def create_sms_status_details(
            self, sms_status_details: storage_dtos.SMSStatusDTO):
        SMSStatusDetails.objects.create(
            sms_provider_id=sms_status_details.sms_provider_id,
            phone_number=sms_status_details.phone_number,
            status=sms_status_details.status)

    def get_sms_provider_configs(
            self, is_active: bool) -> typing.List[storage_dtos.SMSProviderConfigDTO]:
        sms_provider_configs = SMSProviderConfig.objects.filter(
            is_active=is_active)
        return [
            storage_dtos.SMSProviderConfigDTO(
                id=str(sms_provider_config.id),
                sms_provider=sms_provider_config.sms_provider,
                throughput=sms_provider_config.throughput)
            for sms_provider_config in sms_provider_configs
        ]

    def get_failed_msgs(self, status: str) -> typing.List[SMSStatusDetailsDTO]:
        sms_status_details = SMSStatusDetails.objects.filter(
            status=status).prefetch_related("sms_provider")
        return [
            SMSStatusDetailsDTO(
                id=str(each.id),
                phone_number=each.phone_number,
                sms_provider=each.sms_provider.sms_provider)
            for each in sms_status_details
        ]

    def update_sms_status_details(self, sms_status_details_id: str, status: str):
        from django.db.models import F

        SMSStatusDetails.objects.filter(id=sms_status_details_id).update(
            status=status, retrigger_count=F("retrigger_count") + 1)
