'''This module contain user define exceptions for booking,preplan functionality'''


class InvalidDateFormatException(Exception):
    def __init__(self):
        super().__init__("\nInvalid Date Format")
class InvalidDateLessThanPresentException(Exception):
    def __init__(self):
        super().__init__("\nDate can't be less than present date")
class NotEnoughSlotException(Exception):
    def __init__(self):
        super().__init__("\nYou can choose another date")
    

class InvalidNameEmptyException(Exception):
    def __init__(self):
        super().__init__("\nName can't be empty")
class InvalidNameLengthException(Exception):
    def __init__(self):
        super().__init__("\nName can't contain more than 20 character")
class InvalidNameException(Exception):
    def __init__(self):
        super().__init__("\nName can only contain alphabet")
        
        
class InvalidAgeException(Exception):
    def __init__(self):
        super().__init__("\nAge can't be empty or zero or less than 18")
        
        
class InvalidGenderException(Exception):
    def __init__(self):
        super().__init__("\nGender can be only F/M/O")
        


class InvalidCardNumberLengthException(Exception):
    def __init__(self):
        super().__init__("\nCard number must be 16 digits")
class InvalidCardNumberAlphabetException(Exception):
    def __init__(self):
        super().__init__("\nCard number can't contain alphabet")
        
        
        
class InvalidPinLengthException(Exception):
    def __init__(self):
        super().__init__("\nPin must be 4 digits")
class InvalidPinAlphabetException(Exception):
    def __init__(self):
        super().__init__("\nPin can't contain alphabet")
        
class SomethingWrongException(Exception):
    def __init__(self):
        super().__init__("\nSomething went wrong, please try after sometimes")

class CardAlreadySavedException(Exception):
    def __init__(self):
        super().__init__("\nThese card is already saved")