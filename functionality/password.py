'''
Redirected from index.py, This module is for password related issue,
It verify user input using login_password_validations.py from validation package,
interact with database using login_password_db.py from database package,
and use user defined exceptions from login_password_exceptions.py from exception package
'''

import random #importing random to use in OTP creation
from validations import login_password_validations #importing validation module to validate user inputs
from exceptions import login_password_exceptions #importing exception module to get user defined exceptions
from database import login_password_db #importing database module to interact with MySQL database


class Password:
    @staticmethod
    def otpPasswordUpdate(uid, name): #passwoord update using OTP method
        try:
            print("\nPlease enter the 4 digit OPT given: \n")
            otp=random.randrange(1000,9999) #generation OTP
            print("OTP : ",otp)
            c_otp=input("Enter the OTP: ")
            if(otp!=int(c_otp)):
                print("\nWrong OTP, You can't change the password") 
                return
            Password.updatePassword(uid, name) #rediceting to updatepassword function
        
        except login_password_exceptions.SomethingWrongException as e:
            print(e) #If any unexpected db error occur it will redirect to main menu
            return  
        
        except Exception as e:
            print(e)
            choice=input("\nDo you want to continue? 'Y' or 'N':") #If user wants they can go back to otpPasswordUpdate portal or return to main menu
            if(choice.upper()=='Y'):
                Password.otpPasswordUpdate(uid, name) #If user wants they can go back to otpPasswordUpdate portal
            else:
                return #return to main menu
        
        
    @staticmethod
    def updatePassword(uid,name):
        try:
            password=input("\nWelcome "+name+", Enter your new password\n(Lenth must be minimum 8 maximum 20 character)\n(Must contain one capital, one small letter, one number, one special character): ")
            login_password_validations.validatePasswordSyntax(password)
            
            count=0
            while(True):
                c_password=input("Confirm thePassword: ")
                if(login_password_validations.validateConfirmPassword(password, c_password)):
                    break
                else:
                    if(count==1):
                        raise login_password_exceptions.InvalidConfirmPasswordException #if two times password with wrong syntax given throws exception
                    count+=1
            
            sec_qn=None
            print("\nSelect a new secuirity question from below options\n")
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
                        raise login_password_exceptions.InvalidSecurityQuestionOptionException #if two times wronng option choosen throws exception
                    print("\nInvalid Option, Choose again\n")
                    count+=1
            
            sec_ans=input("\nEnter answer for security question\n(Length must be more than 3 character and less than 10 character): ")
            
            sec_ans=login_password_validations.validateSecurityAnswerSyntax(sec_ans)
            login_password_db.updatePassword(uid, password, sec_qn, sec_ans) #updaing new password using database module
            
            print("\nHi "+name+", Your password is successfully changed")
        
        except login_password_exceptions.SomethingWrongException as e:
            print(e) #If any unexpected db error occur it will redirect to main menu
            return #return to main menu
        
        except Exception as e:
            raise e
        
            
    @staticmethod    
    def changePassword():
        try:
            print("\nTo change your password, Kindly follow the steps: \n")
            emailid=input("Enter your email id: ")
            emailid=login_password_validations.validateEmailIdSyntax(emailid)
            info=login_password_db.getPassword(emailid) #getting password information
            if(info[0]==None):
                raise login_password_exceptions.EmailIdNotRegisteredException #if emailid not registeded thwors exception
            
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
                        raise login_password_exceptions.WrongPasswordException #if wrong password three throws exception
                    print("\nWrong Password. Please try again\n") 
                    count+=1
            
            uid=info[0]
            name=info[1].split()[0]
            Password.updatePassword(uid, name) #rediceting to updatepassword function
            
        except login_password_exceptions.EmailIdNotRegisteredException as e:
            print(e)
            print("You may entered a wrong email id")
            choice=input("\nDo you want to try again? 'Y' or 'N' :") #If user wants they can go back to change password portal or main menu
            if(choice.upper()=='Y'):
                Password.changePassword() #If user wants they can go back to change password portal
            else:
                return #return to main menu
        
        except login_password_exceptions.WrongPasswordException as e:
            print(e) #if wrong password three times redirect to forget password
            print("Your account has been locked\n") 
            print("We are redirecting you to Forget Password Protal, Kindly set a new password")
            Password.forgetPassword() #redirect to forget passwrd
            
        except login_password_exceptions.SomethingWrongException as e:
            print(e) #If any unexpected db error occur it will redirect to main menu
            return #return to main menu
        
        except Exception as e:
                print(e)
                choice=input("\nDo you want to continue? 'Y' or 'N' :") #If user wants they can go back to change password portal or return to main menu
                if(choice.upper()=='Y'):
                    Password.changePassword() #If user wants they can go back to change password portal
                else:
                    return #return to main menu
                
                
    @staticmethod
    def forgetPassword():
        try:
            print("\nPyAdventure Forget Password: ")
            print("\nTo set your password, Kindly follow the steps: \n")
            emailid=input("Enter your email id: ")
            emailid=login_password_validations.validateEmailIdSyntax(emailid)
            info=login_password_db.getSecurityQuestionAnswer(emailid) #getting security question and answer
            if(info[0]==None):
                raise login_password_exceptions.EmailIdNotRegisteredException #if emailid not registeded thwors exception
            
            print("\nSelect your secuirity question from below options\n")
            count1=0
            while(True):
                count2=0
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
                            sec_qn="What is your mother's maiden name?"
                            break
                        elif(int(option)==3):
                            sec_qn="What is your pet's name?"
                            break
                        elif(int(option)==4):
                            sec_qn="What is your best friend's name?"
                            break
                        elif(int(option)==5):               
                            sec_qn="What is your favourite movie?"
                            break
                    else:
                        if(count2==1):
                            raise login_password_exceptions.InvalidSecurityQuestionOptionException #if wrong security question option twice throws exception
                        print("\nInvalid Option, Choose again\n")
                        count2+=1
                    
                uid=info[0]
                name=info[1].split()[0]
                if(login_password_validations.validateSecurityQuestion(info[2], sec_qn)):
                    break
                else:
                    if(count1==2):
                        raise login_password_exceptions.WrongSecurityQuestionException #if wrong security question three times throws exception
                    print("\nWrong Question. Please try again\n") 
                    count1+=1
                    
            count=0
            while(True):
                while(True):
                    sec_ans=input("Enter your security answer: ")
                    if(login_password_validations.validateSecurityAnswerIsEmpty(sec_ans)):
                        break
                if(login_password_validations.validateSecurityAnswer(info[3],sec_ans)):
                    break
                else:
                    if(count==2):
                        raise login_password_exceptions.WrongSecurityAnswerException #if wrong security answer three times throws exception
                    print("\nWrong Answer. Please try again\n") 
                    count+=1
                    
            Password.updatePassword(uid, name) #rediceting to updatepassword function
                   
        except login_password_exceptions.EmailIdNotRegisteredException as e:
            print(e)
            print("You may entered a wrong email id")
            choice=input("\nDo you want to try again? 'Y' or 'N' :") #If user wants they can go back to forget password portal or return to main menu
            if(choice.upper()=='Y'):
                Password.forgetPassword() #If user wants they can go back to forget password portal
            else:
                return  #return to main menu
            
        except (login_password_exceptions.WrongSecurityQuestionException ,login_password_exceptions.WrongSecurityAnswerException) as e:
            print(e) #if security question or answer any one is wrong it will go to otpupdatepassword option 
            Password.otpPasswordUpdate(uid, name) #redirecting to otpUpadtePassword function
        
        except login_password_exceptions.SomethingWrongException as e:
            print(e)#If any unexpected db error occur it will redirect to main menu
            return #return to main menu
                     
        except Exception as e:
            print(e)
            choice=input("\nDo you want to continue? 'Y' or 'N':") #If user wants they can go back to forget password portal or return to main menu
            if(choice.upper()=='Y'):
                Password.forgetPassword() #If user wants they can go back to forget password portal
            else:
                return #return to main menu
            
            
    @staticmethod
    def passwordIssue(): #options for password related issue
        print("\nChosse a option from below: \n")
        while(True):
            print("1. Change Password")
            print("2. Forget Password")
            print("3. Exit")
            option=input("\nEnter your choice: ") #redirect accordingly
            if(option.isdigit() and int(option)>0 and int(option)<=3):
                if(int(option)==1):
                    Password.changePassword() #redirect to change password function
                    print("We are redirecting you to the main menu")
                    return
                elif(int(option)==2):
                    Password.forgetPassword() #redirect to forget password function
                    print("We are redirecting you to the main menu")
                    return
                else:
                        return #return to main menu
            else:
                print("\nInvalid Choice. Choose again.\n")
    