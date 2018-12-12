'''This module contain user define exceptions for registration functionality'''


class InvalidNameEmptyException(Exception):
    def __init__(self):
        super().__init__("\nName can't be empty")
class InvalidNameLengthException(Exception):
    def __init__(self):
        super().__init__("\nName can't contain more than 20 character")
class InvalidNameException(Exception):
    def __init__(self):
        super().__init__("\nName can only contain alphabet")
        
        
class InvalidEmailIdSyntaxException(Exception):
    def __init__(self):
        super().__init__("\nThe syntax of Email Id is wrong")
        
             
class InvalidDateFormatException(Exception):
    def __init__(self):
        super().__init__("\nInvalid Date Format")
class InvalidDateGraterThanPresentException(Exception):
    def __init__(self):
        super().__init__("\nBirthday can't be grater than present date")


class InvalidContactNumberLengthException(Exception):
    def __init__(self):
        super().__init__("\nContact number must be 10 digits")
class InvalidContactNumberAlphabetException(Exception):
    def __init__(self):
        super().__init__("\nContact number can't contain alphabet")


class InvalidPasswordSyntaxException(Exception):
    def __init__(self):
        super().__init__("\nInvalid Password Syntax")        
class InvalidConfirmPasswordException(Exception):
    def __init__(self):
        super().__init__("\nYou have entered wrong confirm password twice")
   
        
class InvalidSecurityQuestionOptionException(Exception):
    def __init__(self):
        super().__init__("\nYou have choosen wrong option twice")       
class InvalidSecurityAnswerEmptyException(Exception):
    def __init__(self):
        super().__init__("\nSecurity answer can't be empty")
class InvalidSecurityAnswerLengthException(Exception):
    def __init__(self):
        super().__init__("\nSecurity answer can't contain less than 3 charecter and more than 10 character")
        
        
class InvalidCAPTCHAException(Exception):
    def __init__(self):
        super().__init__("\nYou have entered wrong CAPTCHA twice")
                
        
class EmailAlreadyPresentException(Exception):
    def __init__(self):
        super().__init__("\nEmail id already registered\n")
        

class SomethingWrongException(Exception):
    def __init__(self):
        super().__init__("\nSomething went wrong, please try after sometimes")