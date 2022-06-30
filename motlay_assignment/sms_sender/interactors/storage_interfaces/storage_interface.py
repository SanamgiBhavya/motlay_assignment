import abc
import typing

from sms_sender.interactors.dtos import SMSStatusDetailsDTO
from sms_sender.interactors.storage_interfaces.dtos import \
    SMSStatusDTO, SMSProviderConfigDTO


class StorageInterface:
    @abc.abstractmethod
    def create_sms_status_details(
            self, sms_status_details: SMSStatusDTO):
        pass

    @abc.abstractmethod
    def get_sms_provider_configs(
            self, is_active: bool) -> typing.List[SMSProviderConfigDTO]:
        pass

    @abc.abstractmethod
    def get_failed_msgs(self, status: str) -> typing.List[SMSStatusDetailsDTO]:
        pass

    @abc.abstractmethod
    def update_sms_status_details(self, sms_status_details_id: str, status: str):
        pass
