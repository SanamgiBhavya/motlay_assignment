from dataclasses import dataclass


@dataclass()
class TokenDetailsDTO:
    access_token: str
    refresh_token: str


@dataclass()
class SMSStatusDetailsDTO:
    sms_provider: str
    phone_number: str
    id: str
