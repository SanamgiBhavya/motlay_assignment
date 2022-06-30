class TwilioService:

    def send_message(self, phone_number: str, message: str):
        from twilio.rest import Client
        from django.conf import settings

        client = Client(settings.TWILIO_CLIENT_ACCOUNT_ID, settings.TWILIO_CLIENT_AUTH_TOKEN)
        response = client.messages.create(
            to=phone_number, from_=settings.TWILIO_FROM_MOBILE_NUMBER, body=message)

        return response
