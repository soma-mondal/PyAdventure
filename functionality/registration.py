'''
Redirected from index.py, This module is for registering a new user,
It verify user input using registration_validations.py from validation package,
Create User object to temporalily store user information using pyadventure_class.py from classes package,
Insert user data into database using registration_db.py from database package,
and use user defined exceptions from registratin_exceptions.py from exception package
'''

import random #importing random to use in CAPTCHA creation
from classes.pyadventure_class import User #importing of User class 
from validations import registration_validations #importing validation module to validate user inputs
from exceptions import registration_exceptions #importing exception module to get user defined exceptions
from database import registration_db #importing database module to interact with MySQL database
from functionality.login import Login #importing Login class to redirect to login funtion if email id already registered
from functionality.login_after import LoginAfter #importing LoginAfter class


class Registration:
    @staticmethod
    def createCaptcha(): #generate random CAPTCHA
        captcha_list=list(range(48,58))+list(range(65,91))+list(range(97,123)) #A list which contain ASCII value of digit,capital letter,small letter
        captcha=""
        i=5
        while(i>0):
            captcha+=chr(random.choice(captcha_list))
            i=i-1
        return captcha #returning the CAPTCHA
    
    
    @staticmethod
    def registration():
        try:
            print("\nPyadventure Registration: \n")
            name=input("Enter Name: ")
            name=registration_validations.validateName(name)
            emailid=input("Enter Email Id: ")
            emailid=registration_validations.validateEmailIdSyntax(emailid)
            dateofbirth=input("Enter Date of Birth(dd-mm-yyyy): ")
            dateofbirth=registration_validations.validateDateofbirth(dateofbirth)
            contact_no=input("Enter Contact Number: ")
            contact_no=registration_validations.validateContactNumber(contact_no)
            password=input("Enter Password\n(Lenth must be minimum 8 maximum 20 character)\n(Must contain one capital, one small letter, one number, one special character): ")
            registration_validations.validatePassword(password)
            
            count=0
            while(True):
                c_password=input("Confirm thePassword: ")
                if(registration_validations.validateConfirmPassword(password, c_password)):
                    break
                else:
                    if(count==1):
                        raise registration_exceptions.InvalidConfirmPasswordException #if two times wronng password given throws exception
                    count+=1
            
            sec_qn=None
            print("\nSelect a security question from below options\n")
            count=0
            while(True):
                print("1. What is your favourite book? ")
                print("2. What is your mother's maiden name?")
                print("3. What is your pet's name?")
                print("4. What is your best friend's name?")
                print("5. What is your favourite movie?")
                option=input("\nEnter your choice: ")
                if(option.isdigit() and int(option)>0 and int(option)<=5):
                    if(int(option)==1):
                        sec_qn="What is your favourite book?"
                        break
                    elif(int(option)==2):
                        sec_qn="What is your mother''s maiden name?"
                        break
                    elif(int(option)==3):
                        sec_qn="What is your pet''s name?"
                        break
                    elif(int(option)==4):
                        sec_qn="What is your best friend''s name?"
                        break
                    elif(int(option)==5):               
                        sec_qn="What is your favourite movie?"
                        break
                else:
                    if(count==1):
                        raise registration_exceptions.InvalidSecurityQuestionOptionException #if two times wronng option choosen throws exception
                    print("\nInvalid Option, Choose again\n")
                    count+=1
                    
            sec_ans=input("\nEnter answer for security question\n(Length must be more than 3 character and less than 10 character): ")
            sec_ans=registration_validations.validateSecurityAnswerSyntax(sec_ans)
            
            captcha=Registration.createCaptcha()
            print("\nCAPTCHA: ", captcha)
            count=0
            while(True):
                user_captcha=input("Enter the above given CAPTCHA: ")
                if(registration_validations.validateCAPTCHA(captcha, user_captcha)):
                    break
                else:
                    if(count==1):
                        raise registration_exceptions.InvalidCAPTCHAException #if two times wronng CAPTCHA given throws exception
                    count+=1
            
            user=User(name,emailid,dateofbirth,contact_no,password,sec_qn,sec_ans)
            user=registration_db.userRegistration(user)
            
            name=name.split()[0]
            print("\nWelcome "+name+", Your registration is successfull")
            
            LoginAfter.afterLogin(user.get_uid())
            
                
        except registration_exceptions.EmailAlreadyPresentException as e:
            print(e)
            '''if email id already present it will give a message and if user wants they can go to login page from here'''
            while(True):
                print("1. login")
                print("2. Exit")
                option=input("\nEnter your choice: ")
                '''will redirect according to the choosen option by userc or if wrong option will ask user again to choose'''
                if(option.isdigit() and int(option)>0 and int(option)<=2):
                    if(int(option)==1):
                        uid=Login.login()
                        if(uid!=False): #if successful Login it will return uid(user id) or False
                            LoginAfter.afterLogin(uid)
                            '''Calling afterLogin function to execute parts after Login'''
                        break
                    else:
                        return
                else:
                    print("\nInvalid Choice. Choose again\n")
                        
        except registration_exceptions.SomethingWrongException as e:
            print(e)
            print("We are redirecting you to the main menu") #If any unexpected db error occur it will redirect to main menu
            return
         
        except Exception as e:
            print(e)
            choice=input("\nDo you want to continue? 'Y' or 'N':") #If user wants they can go back to Registration portal or return to main menu
            if(choice.upper()=='Y'):
                Registration.registration() #If user wants they can go back to Registration portal
            else:
                return #return to main menu