import typing

from sms_sender.constants.enums import SMSProvider, SMSStatus
from sms_sender.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from sms_sender.interactors.storage_interfaces.dtos import \
    SMSProviderConfigDTO, SMSStatusDTO
from zappa.asynchronous import task


class SMSProviderInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def sms_provider(
            self, sms_provider_details: SMSProviderConfigDTO,
            phone_numbers: typing.List[str], text: str):

        if sms_provider_details.sms_provider == SMSProvider.JIO.value:
            send_sms_using_twilio_service(
                sms_provider_details=sms_provider_details,
                phone_numbers=phone_numbers, text=text)
        elif sms_provider_details.sms_provider == SMSProvider.AIRTEL.value:
            # For now added twilio for jio also. Will change it.
            send_sms_using_twilio_service(
                sms_provider_details=sms_provider_details,
                phone_numbers=phone_numbers, text=text)


@task
def send_sms_using_twilio_service(
        sms_provider_details: SMSProviderConfigDTO,
        phone_numbers: typing.List[str], text: str):

    from sms_sender.services.twillio_service import TwilioService
    from sms_sender.storages.storage_implementation \
        import StorageImplementation
    from sms_sender.constants.constants import TWILIO_SUCCESS_RESPONSE_STATUS

    storage = StorageImplementation()
    twilio_service = TwilioService()
    for each_phone_number in phone_numbers:
        response = twilio_service.send_message(
            phone_number=each_phone_number, message=text)
        if response.status == TWILIO_SUCCESS_RESPONSE_STATUS:
            sms_status_details = SMSStatusDTO(
                sms_provider_id=sms_provider_details.id,
                phone_number=each_phone_number,
                status=SMSStatus.SENT.value)
        else:
            sms_status_details = SMSStatusDTO(
                sms_provider_id=sms_provider_details.id,
                phone_number=each_phone_number,
                status=SMSStatus.FAILED.value)

        storage.create_sms_status_details(
            sms_status_details=sms_status_details)
