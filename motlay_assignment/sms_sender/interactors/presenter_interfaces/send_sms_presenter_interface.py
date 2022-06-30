import abc
import typing

from django.http.response import HttpResponse


class SendSMSPresenterInterface:

    @abc.abstractmethod
    def raise_invalid_phone_number_exception(
            self, phone_number: typing.List[str]) -> HttpResponse:
        pass

    @abc.abstractmethod
    def raise_no_sms_provider_configs_exists_exception(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def get_success_response(self) -> HttpResponse:
        pass
