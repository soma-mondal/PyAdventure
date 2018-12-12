'''This is the index page of the PyAdventure Application,
This page will redirect to different module according to users choice'''


from functionality.registration import Registration #importing Registration class 
from functionality.login import Login #importing Login class
from functionality.login_after import LoginAfter #importing LoginAfter class
from functionality.password import Password #importing Password class
from functionality.admin_menu import Admin #importing Admin class
from functionality.find_adventure import FindAdventure #importing FindAdventure class


def menu(option): #menu will redirect according to the choosen option by user
    if(int(option)==6):
        print("Thank You")  
        return False #Terminating the programm if user wants to quit
    if(int(option)==1):
        Registration.registration() 
        '''Redirection to registration functionality by calling registration function using class name Registration
           registration is a static function. We can call without object'''
    elif(int(option)==2):
        uid=Login.login()
        '''Redirection to login functionality by calling login function using class name Login
           login is a static function. We can call without object,login function will return the user id if succfull login, so the we can continue'''
        if(uid!=False): #if successful Login it will return uid(user id) or False
            LoginAfter.afterLogin(uid)
            '''Calling afterLogin function to execute parts after Login'''
    elif(int(option)==3):
        Password.passwordIssue()
        '''Redirection to passwprdIssue functionality by calling passwordIssue function using class name Password
           passwprdIssue function has bith option hange password and forget password
           passwprdIssue is a static function. We can call without object'''
    elif(int(option)==4):
        Admin.adminMenu()
        '''Redirection to adminMenu functionality by calling adminMenu function using class name Admin
           adminMenu function is a static function. We can call without object'''
    elif(int(option)==5):
        try:            
            FindAdventure.findAdventure(None)
            
        except Exception as e:
            print(e)
            print("We are redirecting you to the main menu") #If any unexpected db error occur it will redirect to main menu
    print()
    return True
    
        
if __name__ == '__main__': 
    print("+--------------------------+")
    print("|  Welcome to PyAdventure  |")
    print("+--------------------------+\n")
    print("Choose an option from below:\n")
    
    condition=True
    while(condition):
        print("1. New User? Register")
        print("2. Existing User? Login")
        print("3. Change Password/Forget password")
        print("4. Admin Menu")
        print("5. Find your adventure")
        print("6. Quit")
        option=input("\nEnter your choice: ")
        if(option.isdigit() and int(option)>0 and int(option)<=6):
            condition=menu(option) #calling menu which will redirect according to the choosen option by user
        else:
            print("\nPlease enter a valid option 1,2,3,4,5,6.\n") #If user choose a wrong option