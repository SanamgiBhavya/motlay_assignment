from sms_sender.utils.base_enum import BaseEnum


class SMSProvider(BaseEnum):
    AIRTEL = "AIRTEL"
    JIO = "JIO"
    BSNL = "BSNL"


class SMSStatus(BaseEnum):
    SENT = "SENT"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
