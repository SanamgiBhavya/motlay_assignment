import typing

from django.http import HttpResponse
from sms_sender.interactors.presenter_interfaces.send_sms_presenter_interface \
    import SendSMSPresenterInterface
from sms_sender.presenters.mixins.get_error_response_object import GetErrorResponseObject


class SendSMSPresenterImplementation(SendSMSPresenterInterface, GetErrorResponseObject):
    def raise_no_sms_provider_configs_exists_exception(self) -> HttpResponse:
        from sms_sender.constants.exception_messages \
            import NO_SMS_PROVIDER_CONFIGS_EXISTS_EXCEPTION
        return self.get_error_response_object(
            error_constant=NO_SMS_PROVIDER_CONFIGS_EXISTS_EXCEPTION)

    def raise_invalid_phone_number_exception(self, phone_number: typing.List[str]) -> HttpResponse:
        from sms_sender.constants.exception_messages \
            import INVALID_PHONE_NUMBER_EXCEPTION
        import json
        from django.http.response import HttpResponse

        error_constant = INVALID_PHONE_NUMBER_EXCEPTION
        data = {
            "status_code": error_constant[2],
            "message": error_constant[0].format(phone_number),
            "res_status": error_constant[1]
        }
        return HttpResponse(content=json.dumps(data), status=error_constant[2])

    def get_success_response(self) -> HttpResponse:
        from django.http.response import HttpResponse

        return HttpResponse(content="Sent Success", status=200)
