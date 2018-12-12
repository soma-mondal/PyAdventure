'''
Excute only after a successful login from user
'''


from functionality.find_adventure import FindAdventure #importing FindAdventure class
from functionality.booking import Booking #importing Booking class
from functionality.preplan import Preplan #importing Preplan class


class LoginAfter:
    @staticmethod        
    def afterLogin(uid):
        try:
            #after successfull loging options for user
            while(True):
                print("\nChosse a option from below\n") 
                print("1. Find your adventure")
                print("2. Check your preplaned adventure")
                print("3. Show booking details")
                print("4. Logout")
                option=input("\nEnter your choice: ")
                if(option.isdigit() and int(option)>0 and int(option)<=4): #redirect accordingly
                    if(int(option)==1):
                        FindAdventure.findAdventure(uid)
                    elif(int(option)==2):
                        Preplan.showPreplan(uid)
                    elif(int(option)==3):
                        Booking.showBooking(uid)
                    else:
                        return
                else:
                    print("\nInvalid Choice. Choose again\n")
         
        except Exception as e:
            print(e)
            print("We are redirecting you to the main menu") #If any unexpected db error occur it will redirect to main menu
            return