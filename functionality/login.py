'''
Redirected from index.py, This module is for login a user,
It verify user input using login_password_validations.py from validation package,
interact with database using login_password_db.py from database package,
and use user defined exceptions from login_password_exceptions.py from exception package
'''


from validations import login_password_validations #importing validation module to validate user inputs
from exceptions import login_password_exceptions #importing exception module to get user defined exceptions
from database import login_password_db #importing database module to interact with MySQL database
from functionality.password import Password #importing Password class to redirect to forgrtPassword funtion if account is locked


class Login:
    @staticmethod
    def login():
        try:
            print("\nPyadventure Login: \n")
            emailid=input("Enter your email id: ")
            login_password_validations.validateEmailIdSyntax(emailid)
            info=login_password_db.getPassword(emailid)
            if(info[0]==None):
                raise login_password_exceptions.EmailIdNotRegisteredException #if emailid not registered throes exception
                
            count=0
            while(True):
                while(True):
                    password=input("Enter yout password: ")
                    if(login_password_validations.validatePasswordIfEmpty(password)):
                        break
                if(login_password_validations.validatePassword(info[2],password)):
                    break
                else:
                    if(count==2):
                        raise login_password_exceptions.WrongPasswordException #if three times worng password throes exception
                    print("\nWrong Password. Please try again\n") 
                    count+=1
            
            uid=int(info[0])
            name=info[1].split()[0]
            print("\nWelcome back "+name)
            return uid
            
        except login_password_exceptions.EmailIdNotRegisteredException as e:
            print(e)
            print("You may entered a wrong email id")
            choice=input("\nDo you want to try again? 'Y' or 'N' :") #If user wants they can go back to login portal or return to main menu
            if(choice.upper()=='Y'):
                return Login.login() #If user wants they can go back to login portal
            else:
                return False#return to main menu
        
        except login_password_exceptions.WrongPasswordException as e:
            print(e) #if wrong password redirect to forget password
            print("Your account has been locked\n") 
            print("We are redirecting you to Forget Password Protal, Kindly set a new password")
            Password.forgetPassword()
            choice=input("\nDo you want to login? 'Y' or 'N': ") #If user wants they can go to login portal or return to main menu
            if(choice.upper()=='Y'):
                return Login.login() #If user wants they can go to login portal
            else:
                return False#return to main menu
            
        except login_password_exceptions.SomethingWrongException as e:
            print(e)
            print("We are redirecting you to the main menu") #If any unexpected db error occur it will redirect to main menu
            return False
            
        except Exception as e:
                print(e)
                choice=input("\nDo you want to continue? 'Y' or 'N': ") #If user wants they can go back to login portal or return to main menu
                if(choice.upper()=='Y'):
                    return Login.login()  #If user wants they can go back to login portal
                else:
                    return False#return to main menu
    
