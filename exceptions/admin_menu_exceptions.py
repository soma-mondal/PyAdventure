'''This module contain user define exceptions for admin_menu functionality'''


class InvalidNameEmptyException(Exception):
    def __init__(self):
        super().__init__("\nName can't be empty")
class InvalidNameLengthException(Exception):
    def __init__(self):
        super().__init__("\nName can't contain more than 50 character")
class InvalidNameException(Exception):
    def __init__(self):
        super().__init__("\nName can only contain alphabet")
        
        
class InvalidDescriptionEmptyException(Exception):
    def __init__(self):
        super().__init__("\nDescription can't be empty")
class InvalidDescriptionLengthException(Exception):
    def __init__(self):
        super().__init__("\nDescriptione can't contain more than 500 character")
class InvalidDescriptionException(Exception):
    def __init__(self):
        super().__init__("\nDescription can't contain only number")
        
        
class InvalidPlaceEmptyException(Exception):
    def __init__(self):
        super().__init__("\nPlace can't be empty")
class InvalidPlaceLengthException(Exception):
    def __init__(self):
        super().__init__("\nPlace can't contain more than 50 character")
class InvalidPlaceException(Exception):
    def __init__(self):
        super().__init__("\nPlace can't contain only number")
        
        
        
class InvalidPriceEmptyException(Exception):
    def __init__(self):
        super().__init__("\nPrice can't be empty")
class InvalidPriceAlphabetException(Exception):
    def __init__(self):
        super().__init__("\nPrice can't contain alphabet")
        
        
class InvalidSlotEmptyException(Exception):
    def __init__(self):
        super().__init__("\nSlot can't be empty")
class InvalidSlotAlphabetException(Exception):
    def __init__(self):
        super().__init__("\nSlot can't contain alphabet")
        
        
class SomethingWrongException(Exception):
    def __init__(self):
        super().__init__("\nSomething went wrong, please try after sometimes")