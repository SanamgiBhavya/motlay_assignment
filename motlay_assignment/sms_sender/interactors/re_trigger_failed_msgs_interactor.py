from sms_sender.constants.enums import SMSStatus, SMSProvider
from sms_sender.interactors.storage_interfaces.storage_interface \
    import StorageInterface


class RetriggerFailedMSGInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def retrigger_failed_msgs(self):
        failed_msgs = self.storage.get_failed_msgs(status=SMSStatus.FAILED.value)
        for each in failed_msgs:
            if each.sms_provider == SMSProvider.TWILIO.value:
                from sms_sender.services.twillio_service import TwilioService
                from sms_sender.constants.constants import TWILIO_SUCCESS_RESPONSE_STATUS

                twilio_service = TwilioService()
                response = twilio_service.send_message(
                    phone_number=each.phone_number, message="text")
                if response.status == TWILIO_SUCCESS_RESPONSE_STATUS:
                    self.storage.update_sms_status_details(
                        sms_status_details_id=each.id, status=SMSStatus.SENT.value)
                else:
                    self.storage.update_sms_status_details(
                        sms_status_details_id=each.id, status=SMSStatus.FAILED.value)
