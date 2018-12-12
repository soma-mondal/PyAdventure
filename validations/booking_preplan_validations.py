'''This module is used to validate user given inputs in boooking,preplan module'''


from exceptions import booking_preplan_exceptions
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



def validateDate(date): #validate the given date syntax and also is it past date or not
    date=compress(date)
    date=date.split('-')
    if(len(date)!=3): 
        raise booking_preplan_exceptions.InvalidDateFormatException #if not use two --(dash) in between date,month,year throws exception 
    if(len(date[0])!=2 or len(date[1])!=2 or len(date[2])!=4):
        raise booking_preplan_exceptions.InvalidDateFormatException #if do not use dd-mm-yyyy format throws exception
    if(date[0].isdigit()==False or date[1].isdigit()==False or date[1].isdigit()==False):
        raise booking_preplan_exceptions.InvalidDateFormatException #if give any alphabet as dd,mm,yyyy throws exception
    date_given=datetime(int(date[2]),int(date[1]),int(date[0])) 
    present=datetime.now()
    if(date_given<present):
        raise booking_preplan_exceptions.InvalidDateLessThanPresentException #if it is past date throws exception as dateofbirth must be a past date
    return date[2]+"-"+date[1]+"-"+date[0] #return the date as yyyy-mm-dd format as MySQL database take date in this fromat 



def validateName(name):  #validate the given name
    name=compress(name)
    if(name==""):
        raise booking_preplan_exceptions.InvalidNameEmptyException #if empty throws exception
    if(len(name)>20):
        raise booking_preplan_exceptions.InvalidNameLengthException #if more than 20 character throws exception 
    name_list=name.split()
    for i in name_list:
        if(i.isalpha()==False):
            raise booking_preplan_exceptions.InvalidNameException #if contain any numeric throws exception
    return name

def validateAge(age): #validate given age
    age=compress(age)
    if(age==""):
        raise booking_preplan_exceptions.InvalidAgeException #if empty throws exception
    if(int(age)<18):
        raise booking_preplan_exceptions.InvalidAgeException #if less than 18 throws exception
    return age


def validateGender(gendar): #validate given gendar
    gendar=compress(gendar)
    gendar=gendar.upper()
    if(gendar!="F" and gendar!="M" and gendar!="O"):
        raise booking_preplan_exceptions.InvalidGenderException #if not M/F/O throws exception
    return gendar


def validateCardNumber(card_no): #validaate given card number
    card_no=compress(card_no)
    if(len(card_no)!=16):
        raise booking_preplan_exceptions.InvalidCardNumberLengthException #must be lenth 16 else throws exception
    if(card_no.isdigit()==False):
        raise booking_preplan_exceptions.InvalidCardNumberAlphabetException #can't contaion any alphabet else throws exception
    return card_no    


def validateCardExpiry(date): #valdite given expiry date
    date=compress(date)
    date=date.split('/')
    if(len(date)!=2): 
        raise booking_preplan_exceptions.InvalidDateFormatException #if not use two --(dash) in between date,month,year throws exception 
    if(len(date[0])!=2 or len(date[1])!=4):
        raise booking_preplan_exceptions.InvalidDateFormatException #if do not use dd-mm-yyyy format throws exception
    if(date[0].isdigit()==False or date[1].isdigit()==False):
        raise booking_preplan_exceptions.InvalidDateFormatException #if give any alphabet as dd,mm,yyyy throws exception
    mon_set_31=[1,3,5,7,8,10,12]
    mon_set_30=[4,6,9,11]
    if(int(date[0])==2):
        if(int(date[1])%400==0 or ((int(date[1])%4==0) and (int(date[1])%100 !=0))):
            date_given=datetime(int(date[1]),int(date[0]),28) 
        else:
            date_given=datetime(int(date[1]),int(date[0]),29) 
    elif(int(date[0]) in mon_set_30):
        date_given=datetime(int(date[1]),int(date[0]),30) 
    elif(int(date[0]) in mon_set_31):
        date_given=datetime(int(date[1]),int(date[0]),31) 
    present=datetime.now()
    if(date_given<present):
        raise booking_preplan_exceptions.InvalidDateLessThanPresentException #if it is not past date throws exception as dateofbirth must be a past date
    return date[0]+"/"+date[1] #return the date as yyyy-mm-dd format as MySQL database take date in this fromat 


def validatePin(pin): #validate pin
    pin=compress(pin)
    if(len(pin)!=4):
        raise booking_preplan_exceptions.InvalidPinLengthException #must be lenth 4 else throws exception
    if(pin.isdigit()==False):
        raise booking_preplan_exceptions.InvalidPinAlphabetException #can't contaion any alphabet else throws exception
    return pin  


