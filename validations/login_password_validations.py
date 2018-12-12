'''This module is used to validate user given inputs in login and password module'''


import re #importing regular expression for password and emailid validation
from exceptions import login_password_exceptions #importinf user defined exceptions


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


def validateEmailIdSyntax(emailid): #validate syntax of given email id
    emailid=compress(emailid)
    if(re.search(r'^[-\w\+]+(\.[-\w\+]+)*@[a-zA-Z0-9]+\w*\.\w*[a-zA-Z0-9]+$', emailid)==None):
        raise login_password_exceptions.InvalidEmailIdSyntaxException #if basic emailid syntax doesn't match throws exception
    return emailid


def validatePasswordIfEmpty(password): #check if user is entering any password or keeping empty
    if " " in password or password=="":
        print("passwor can't be empty or contain space")
        return False
    return True


def validatePassword(actual_password,given_password): #checking if user entered password is right
    if(given_password!=actual_password):
        return False
    return True


def validatePasswordSyntax(password):  #validate syntax of given password mentioned in application
    if " " in password:
        raise login_password_exceptions.InvalidPasswordSyntaxException #if empty throws exception
    if(len(password)<8 or len(password)>20):
        raise login_password_exceptions.InvalidPasswordSyntaxException #if not greter than 8 and less than 20 throws exception
    if(re.search(r'[a-z]', password)!=None and re.search(r'[A-Z]', password)!=None and re.search(r'[0-9]', password)!=None and re.search(r'[-`~!@#\$%\^&\*\(\)_=\+\[\]\{\}\|\:;"<>,./\?]', password)!=None):
        return
    raise login_password_exceptions.InvalidPasswordSyntaxException#if the application given syntax do not match throws exceptios


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


def validateSecurityQuestion(actual_question,given_question): #checking if user entered question is right
    if(given_question!=actual_question):
        return False
    return True


def validateSecurityAnswerIsEmpty(ans): #check if user is entering any answer or keeping empty
    if(ans==""):
        print("passwor can't be empty")
        return False
    if(len(ans.split())==0):
        print("passwor can't be empty")
        return False
    return True


def validateSecurityAnswer(actual_ans,given_ans): #checking if user entered answer is right
    if(given_ans!=actual_ans):
        return False
    return True    


def validateSecurityAnswerSyntax(sec_ans): #validate the given security answer
    sec_ans=compress(sec_ans)
    if(sec_ans==""):
        raise login_password_exceptions.InvalidSecurityAnswerEmptyException #if empty throws exception
    if(len(sec_ans)<3 or len(sec_ans)>10):
        raise login_password_exceptions.InvalidSecurityAnswerLengthException #if not greter than 3 and less than 10 throws exception
    return sec_ans