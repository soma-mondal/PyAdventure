'''This module is used to validate user given inputs in registration module'''


import re #importing regular expression for password and emailid validation
from exceptions import registration_exceptions #importinf user defined exceptions
from datetime import datetime #importing datetime module for date validation

def compress(data): #used to compress the data if there is any leading or tailing spaces
    start=None
    for i in range(0,len(data)):
        if(data[i]!=" "):
            start=i
            break
    if(start!=None):
        data=data[start:]
    end=None
    for i in range(len(data)-1,-1,-1):
        if(data[i]!=" "):
            end=i
            break
    if(end!=None):
        data=data[:end+1]
    if(start==None and end==None):
        return ""
    return data


def validateName(name):  #validate the given name
    name=compress(name)
    if(name==""):
        raise registration_exceptions.InvalidNameEmptyException #if empty throws exception
    if(len(name)>20):
        raise registration_exceptions.InvalidNameLengthException #if more than 20 character throws exception 
    name_list=name.split()
    for i in name_list:
        if(i.isalpha()==False):
            raise registration_exceptions.InvalidNameException #if contain any numeric throws exception
    return name
        
        
def validateEmailIdSyntax(emailid): #validate syntax of given email id
    emailid=compress(emailid)
    if(re.search(r'^[-\w\+]+(\.[-\w\+]+)*@[a-zA-Z0-9]+\w*\.\w*[a-zA-Z0-9]+$', emailid)==None):
        raise registration_exceptions.InvalidEmailIdSyntaxException #if basic emailid syntax doesn't match throws exception
    return emailid


def validateDateofbirth(date): #validate the given date syntax and also is it past date or not
    date=compress(date)
    date=date.split('-')
    if(len(date)!=3): 
        raise registration_exceptions.InvalidDateFormatException #if not use two --(dash) in between date,month,year throws exception 
    if(len(date[0])!=2 or len(date[1])!=2 or len(date[2])!=4):
        raise registration_exceptions.InvalidDateFormatException #if do not use dd-mm-yyyy format throws exception
    if(date[0].isdigit()==False or date[1].isdigit()==False or date[1].isdigit()==False):
        raise registration_exceptions.InvalidDateFormatException #if give any alphabet as dd,mm,yyyy throws exception
    date_given=datetime(int(date[2]),int(date[1]),int(date[0])) 
    present=datetime.now()
    if(date_given>present):
        raise registration_exceptions.InvalidDateGraterThanPresentException #if it is not past date throws exception as dateofbirth must be a past date
    return date[2]+"-"+date[1]+"-"+date[0] #return the date as yyyy-mm-dd format as MySQL database take date in this fromat 


def validateContactNumber(contact_no): #validate the given contact number
    contact_no=compress(contact_no)
    if(len(contact_no)!=10):
        raise registration_exceptions.InvalidContactNumberLengthException #must be lenth 10 else throws exception
    if(contact_no.isdigit()==False):
        raise registration_exceptions.InvalidContactNumberAlphabetException #can't contaion any alphabet else throws exception
    return contact_no


def validatePassword(password): #validate syntax of given password mentioned in application
    if " " in password:
        raise registration_exceptions.InvalidPasswordSyntaxException #if empty throws exception
    if(len(password)<8 or len(password)>20):
        raise registration_exceptions.InvalidPasswordSyntaxException #if not greter than 8 and less than 20 throws exception
    if(re.search(r'[a-z]', password)!=None and re.search(r'[A-Z]', password)!=None and re.search(r'[0-9]', password)!=None and re.search(r'[-`~!@#\$%\^&\*\(\)_=\+\[\]\{\}\|\:;"<>,./\?]', password)!=None):
        return 
    raise registration_exceptions.InvalidPasswordSyntaxException #if the application given syntax do not match throws exceptios


def validateConfirmPassword(password,c_password): #validate the confirm password
    if(c_password==""):
        print("Confirm password can't be empty. Please enter again") 
        return
    temp=c_password
    if(len(temp.split())==0):
        print("Confirm password can't be empty. Please enter again") 
        return
    if(password!=c_password):
        print("Password and confirm password do not match. Please enter again") 
        return
    if(len(c_password.split())==0):
        print("Confirm password can't be empty. Please enter again") 
        return
    return True

    
def validateSecurityAnswerSyntax(sec_ans): #validate the given security answer
    sec_ans=compress(sec_ans)
    if(sec_ans==""):
        raise registration_exceptions.InvalidSecurityAnswerEmptyException #if empty throws exception
    if(len(sec_ans)<3 or len(sec_ans)>10):
        raise registration_exceptions.InvalidSecurityAnswerLengthException #if not greter than 3 and less than 10 throws exception
    return sec_ans


def validateCAPTCHA(captcha,user_captcha): #validate user's entered CAPTCHA
    user_captcha=compress(user_captcha)
    if(user_captcha==""):
        print("\nCAPTCHA can't be empty. Please try again\n")
        return
    temp=user_captcha
    if(len(temp.split())==0):
        print("\nCAPTCHA can't be empty. Please try again\n")
        return
    if(captcha!=user_captcha):
        print("\nWrong CAPTCHA. Please try again\n")
        return    
    return True

