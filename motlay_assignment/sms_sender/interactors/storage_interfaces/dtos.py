from dataclasses import dataclass


@dataclass()
class SMSProviderConfigDTO:
    id: str
    sms_provider: str
    throughput: int


@dataclass()
class SMSStatusDTO:
    sms_provider_id: str
    phone_number: str
    status: str
