from rest_framework import serializers


class SendSMSValidationSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    phone_numbers = serializers.ListField(
        child=serializers.CharField(read_only=True))
