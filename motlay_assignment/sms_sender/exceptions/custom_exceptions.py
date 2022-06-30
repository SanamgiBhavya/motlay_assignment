class InvalidPhoneNumbersException(Exception):

    def __init__(self, invalid_phone_numbers):
        self.invalid_phone_numbers = invalid_phone_numbers


class IncorrectPasswordException(Exception):
    pass


class UserDoesNotExistException(Exception):
    pass


class UnexpectedErrorOccurredToGetTokenDetailsException(Exception):
    pass


class NoSMSProviderConfigsExistsException(Exception):
    pass
