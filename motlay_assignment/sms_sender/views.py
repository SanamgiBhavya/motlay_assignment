from rest_framework.views import APIView
from sms_sender.serializers.validation_serializers import\
    SendSMSValidationSerializer


class SendSMSView(APIView):
    def post(self, request):
        request_data = request.data
        serializers = SendSMSValidationSerializer(data=request_data)
        if serializers.is_valid(raise_exception=True):
            from sms_sender.interactors.send_sms_interactor import SendSMSInteractor
            from sms_sender.storages.storage_implementation import StorageImplementation
            from sms_sender.presenters.send_sms_presenter_implementation import SendSMSPresenterImplementation
            storage = StorageImplementation()
            interactor = SendSMSInteractor(storage=storage)
            response = interactor.send_sms_wrapper(
                phone_numbers=request_data["phone_numbers"],
                text=request_data["text"], presenter=SendSMSPresenterImplementation())
            return response
