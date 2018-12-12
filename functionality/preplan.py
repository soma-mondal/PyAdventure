'''execute if user wants to save an adventure as preplan'''


from validations import booking_preplan_validations #importing validation module to validate user inputs
from exceptions import booking_preplan_exceptions #importing exception module to get user defined exceptions
from database import booking_preplan_db #importing database module to interact with MySQL database
from functionality.booking import Booking #importing Booking class

 
class Preplan:
    def __init__(self,uid,aid,name,place,amount_per_person):
        self.__pid=None
        self.__uid=uid
        self.__aid=aid
        self.__name=name
        self.__place=place
        self.__date=None
        self.__amount_per_person=amount_per_person
        self.__no_of_slots=None
        self.__total_amount=None
        
        
    def get_pid(self):
        return self.__pid
    def get_uid(self):
        return self.__uid
    def get_aid(self):
        return self.__aid
    def get_name(self):
        return self.__name
    def get_place(self):
        return self.__place
    def get_date(self):
        return self.__date
    def get_amount_per_person(self):
        return self.__amount_per_person
    def get_no_of_slots(self):
        return self.__no_of_slots
    def get_total_amount(self):
        return self.__total_amount


    def set_bid(self, pid):
        self.__pid = pid
    def set_date(self, date):
        self.__date = date
    def set_no_of_slots(self, no_of_slots):
        self.__no_of_slots = no_of_slots
    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount
        
    @staticmethod
    def changeDateFormat(date):  #changing the date format as MySQL accept date as yyyy-mm-dd format
        date=date.split('-')
        return date[2]+'-'+date[1]+'-'+date[0] 
        
    def preplan(self):
        try:
            print("\nYour Adventure: ",self.__name)
            print("Location: ",self.__place)
            print("Amount per person: ",self.__amount_per_person)
            date=input("Enter Date(dd-mm-yyyy): ")
            date=booking_preplan_validations.validateDate(date)
            no_of_slots_available=booking_preplan_db.getAvailaleSlots(self.__aid, self.__place, date)
            
            if(int(no_of_slots_available)==0):
                print("Sorry, No slots availble for that date")
                raise booking_preplan_exceptions.NotEnoughSlotException #if no slots available for given date raise exception
            
            print("Available Slots: ",no_of_slots_available)
            no_of_people=input("\nEnter no of people: ")
            
            if(int(no_of_people)>int(no_of_slots_available)):
                print("Sorry, not enough slots availble")
                raise booking_preplan_exceptions.NotEnoughSlotException #if no enough slots available for given date and no of people raise exception
            
            self.__date=date
            self.__no_of_slots=no_of_people
            self.__total_amount=int(no_of_people)*int(self.__amount_per_person)
            print("Total amount: ",self.__total_amount)
                  
            choice=input("\nDo you want to save your planing? 'Y' or 'N':") #If user wants they can go back to bookin or return to main menu
            if(choice.upper()=='Y'):
                booking_preplan_db.savePreplan(self)
                print("Your plan is saved successfully")
            else:
                return #return to main menu
            
        except (booking_preplan_exceptions.InvalidDateFormatException,booking_preplan_exceptions.InvalidDateLessThanPresentException,booking_preplan_exceptions.NotEnoughSlotException) as e:
            print(e)
            choice=input("\nDo you want to continue? 'Y' or 'N':") #If user wants they can go back to bookin or return to main menu
            if(choice.upper()=='Y'):
                self.preplan() #If user wants they can go back to booking
            else:
                return #return to main menu
 
        except Exception as e:
            raise e   
        
        
        
    @staticmethod
    def showPreplan(uid):
        try:
            print("\nPyadventure Preplan\n")
            preplan_details=booking_preplan_db.getPreplanDetails(uid)
            if(preplan_details==False):
                print("You don't have any saved preplan")
                return
        
            print("These are your preplan")
            for i in range(0,len(preplan_details[0])):
                    print("\nPreplan "+str(i+1)+":")
                    print("Your Adventur: "+preplan_details[2][i])
                    print("location: "+preplan_details[3][i])
                    date=Preplan.changeDateFormat(str(preplan_details[4][i]))
                    print("Date: "+date)
                    print("Amount per person: ",+preplan_details[5][i])
                    print("No of People: ",+preplan_details[6][i])
                    print("Total Amount: "+str(preplan_details[7][i]))
                    
            choice=input("\nDo you want to book/delete any preplan? 'Y' or 'N': ")
            if(choice.upper()=='Y'): 
                while(True):
                    print("\nSelect your option\n")
                    for i in range(0,len(preplan_details[0])):
                        print(str(i+1)+". Preplan "+str(i+1))
                    option=input("\nEnter your choice: ")
                    if((int(option)>=1 and int(option)<=i+1)==False):
                        print("\nInvalid Option,Choose again")
                    else:
                        break
                    
                while(True):
                    print("\n1. Book this preplan")
                    print("2. Delete this preplan")
                    option_new=input("\nSelect your choice: ")
                    if(option_new.isdigit() and int(option_new)>0 and int(option_new)<=2): #redirect accordingly
                        if(int(option_new)==1):                    
                            pid=int(preplan_details[0][int(option)-1]) #creating preplan attribute
                            aid=int(preplan_details[1][int(option)-1])
                            name=preplan_details[2][int(option)-1]
                            place=preplan_details[3][int(option)-1]
                            price=int(preplan_details[5][int(option)-1])
                            no_of_people=int(preplan_details[6][int(option)-1])
                            
                            booking=Booking(uid,aid,name,place,price) #creating Booking object 
                            booking.preplanbooking(date, no_of_people) #booking that prepln
                            
                            booking_preplan_db.deletePreplan(pid) #deleting the booked preplan
                            break
                        
                        else:
                            pid=int(preplan_details[0][int(option)-1])
                            booking_preplan_db.deletePreplan(pid) #deleteting preplan from database
                            print("\nYour Preplan is deleted successfully")
                            break
                    else:
                        print("\nInvalid Choice. Choose again\n")
            else:
                return 
            
            choice=input("\nDo you want to check preplan again? 'Y' or 'N': ")
            if(choice.upper()=='Y'): 
                Preplan.showPreplan(uid) #if wants to book another preplan
            else:
                return 
            
        except Exception:
            raise booking_preplan_exceptions.SomethingWrongException
        
        
        
