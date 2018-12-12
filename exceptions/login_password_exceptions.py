'''This module contain user define exceptions for login,password functionality'''


class InvalidEmailIdSyntaxException(Exception):
    def __init__(self):
        super().__init__("\nThe syntax of Email Id is wrong")        
class EmailIdNotRegisteredException(Exception):
    def __init__(self):
        super().__init__("\nYour Email Id is not registered with us")
class NotAdminException(Exception):
    def __init__(self):
        super().__init__("\nYou're not an Admin")
        
        
class WrongPasswordException(Exception):
    def __init__(self):
        super().__init__("\nYou have entered wrong password three times")
class InvalidPasswordSyntaxException(Exception):
    def __init__(self):
        super().__init__("\nInvalid Password Syntax")
class InvalidConfirmPasswordException(Exception):
    def __init__(self):
        super().__init__("\nYou have entered wrong confirm password twice")
        
        
class InvalidSecurityQuestionOptionException(Exception):
    def __init__(self):
        super().__init__("\nYou have choosen wrong option twice")
class WrongSecurityQuestionException(Exception):
    def __init__(self):
        super().__init__("\nYou have choosen wrong security question three times")
class WrongSecurityAnswerException(Exception):
    def __init__(self):
        super().__init__("\nYou have entered wrong security answer three times")
class InvalidSecurityAnswerEmptyException(Exception):
    def __init__(self):
        super().__init__("\nSecurity answer can't be empty")
class InvalidSecurityAnswerLengthException(Exception):
    def __init__(self):
        super().__init__("\nSecurity answer can't contain less than 3 charecter and more than 10 character")
        
        
class SomethingWrongException(Exception):
    def __init__(self):
        super().__init__("\nSomething went wrong, please try after sometimes")