'''
Redirected from index.py, This module is for login a user,
user can book or save adventure as preplan from here
'''


from database import find_adventure_db #importing database module to interact with MySQL database
from functionality.login import Login #importing Login class
from functionality.booking import Booking #importing Booking class
from functionality.preplan import Preplan #importing Preplan class


class SomethingWrongException(Exception): #creating user defined exceptions
    def __init__(self):
        super().__init__("\nSomething went wrong, please try after sometimes")

class FindAdventure:
    @staticmethod
    def findAdventure(uid):
        try:
            print("\nPyAdventure Find Your Adventure: \n")
            print("Choose an option from below. \n")
            adventures=find_adventure_db.getAdventures() #get all adventure names as list with aid
            
            while(True): #redirect accordingly
                for i in range(0,len(adventures[0])):
                    print(str(adventures[0][i])+". "+adventures[1][i])
                print("e. Exit")
                option=input("\nEnter your choice: ")
                if(option=='e'):
                    return
                if(int(option) not in adventures[0]):
                    print("\nInvalid Option,Choose again\n")
                else:
                    break
            aid=int(option) #aid of choosen adventure
            name=adventures[1][aid-1] #name of choosen adventure
            description=find_adventure_db.getDescription(aid) #get ddescription associated with choosen adventure
            print("\nYou have choosen: ",name)
            print("Description: ",description)
            print("\nYou can do "+name+" in the following places\n")
            details=find_adventure_db.getAdventureDetails(aid) #get detailes associated with choosen adventure
            
            while(True): #redirect accordingly
                for i in range(0,len(details[0])):
                    print(str(i+1)+". "+details[0][i]+" - "+str(details[1][i]))
                print("e. Exit")
                option=input("\nSelect the place from given list or e for Exit: ")
                if(option=='e'):
                    return
                if((int(option)>=1 and int(option)<=i+1)==False):
                    print("\nInvalid Option,Choose again\n")
                else:
                    break
                
            place=details[0][int(option)-1] #choosen place
            price=details[1][int(option)-1] #price of choosen place
            print("\nYou have choosen: ",place)
            print("Amount per person: ",price)
            
            if(uid==None):
                print("\nTo continue, you must login")
                choice=input("Do you want to login? 'Y' or 'N': ") #If user wants they can go to login portal or return to main menu
                if(choice.upper()=='Y'):
                    uid=Login.login() #If user wants they can go to login portal
                else:
                    return #return to main menu
            if(uid!=False): #
                print("\nChosse a option from below\n")
                while(True):
                    print("1. Booking")
                    print("2. Save as Preplan")
                    option=input("\nEnter your choice: ")
                    if(option.isdigit() and int(option)>0 and int(option)<=2): #redirect accordingly
                        if(int(option)==1):
                            booking=Booking(uid,aid,name,place,price)
                            booking.booking()
                            break
                        else:
                            preplan=Preplan(uid,aid,name,place,price)
                            preplan.preplan()
                            break
                    else:
                        print("\nInvalid Choice. Choose again\n")
            
            else:
                print("\nSorry, you can't continue without Login")
                print("We are redirecting you to the main menu")
                        
        except Exception:
            raise SomethingWrongException