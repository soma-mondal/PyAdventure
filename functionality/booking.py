'''execute if user wants to book an adventure or wants to checked previously booked adventure'''


from validations import booking_preplan_validations #importing validation module to validate user inputs
from exceptions import booking_preplan_exceptions #importing exception module to get user defined exceptions
from database import booking_preplan_db #importing database module to interact with MySQL database


class Booking:
    def __init__(self,uid,aid,name,place,amount_per_person):
        self.__bid=None
        self.__uid=uid
        self.__aid=aid
        self.__name=name
        self.__place=place
        self.__date=None
        self.__amount_per_person=amount_per_person
        self.__no_of_slots=None
        self.__total_amount=None


    def get_bid(self):
        return self.__bid
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


    def set_bid(self, bid):
        self.__bid = bid
    def set_date(self, date):
        self.__date = date
    def set_no_of_slots(self, no_of_slots):
        self.__no_of_slots = no_of_slots
    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount

    @staticmethod
    def changeDateFormat(date): #changing the date format as MySQL accept date as yyyy-mm-dd format
        date=date.split('-')
        return date[2]+'-'+date[1]+'-'+date[0] 
            
    def booking(self):
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
            
            choice=input("\nDo you want to book? 'Y' or 'N':") #If user wants they can go back to bookin or return to main menu
            if(choice.upper()=='Y'):
                self.finalBooking(no_of_people)
            else:
                return #return to main menu
            
        except (booking_preplan_exceptions.InvalidDateFormatException,booking_preplan_exceptions.InvalidDateLessThanPresentException,booking_preplan_exceptions.NotEnoughSlotException) as e:
            print(e)
            choice=input("\nDo you want to continue? 'Y' or 'N':") #If user wants they can go back to bookin or return to main menu
            if(choice.upper()=='Y'):
                self.booking() #If user wants they can go back to booking
            else:
                return #return to main menu
            
        except Exception as e:
            raise e
        
    def finalBooking(self,no_of_people):
        try:
            people_information=Booking.setPeopleInformation(self.__uid,int(no_of_people)) #saving peoples information
            if(people_information==False):
                print("\nSorry, you can't continue without people's information")
                print("We are redirection to main menu")
                return
            
            payment=Booking.payment(self.__uid, self.__total_amount) #doing payment
            if(payment==False):
                print("\nPayment is failed")
                print("Sorry, you can't continue without payment")
                print("We are redirection to main menu")
                return
            
            self=booking_preplan_db.finalBooking(self,people_information) #booking 
            print("\nYour booking is successful")
            print("Your booking id is: ",self.__bid)
            
        except Exception as e:
            raise e
        
    
    @staticmethod
    def setPeopleInformation(uid,no_of_people):
        try: 
            people_info=[]
            count=1
            while(count<=no_of_people):
                print("\nInfromation of person ",count)
                name=input("Enter name: ")
                name=booking_preplan_validations.validateName(name)
                gender=input("Enter Gender(F-Female, M-Male, O-Other): ")
                gender=booking_preplan_validations.validateGender(gender)
                age=input("Enter age (Age must be greter than 18): ")
                age=booking_preplan_validations.validateAge(age)
                people_info.append([name,gender,age])
                count=count+1
                
            return people_info #returning people info as list
        
        except Exception as e:
            print(e)
            choice=input("\nDo you want to try again? 'Y' or 'N':") #If user wants they can go back to set peopple information or return to main menu
            if(choice.upper()=='Y'):
                return Booking.setPeopleInformation(uid, no_of_people) #If user wants they can go back to set peopple information
            else:
                return False#return to main menu
            
            
         
    @staticmethod
    def payment(uid,total_amount):
        try: 
            print("\nOnly online payment mode is available")
            card_details=booking_preplan_db.getCardDetails(uid) #getting saved card details
            
            if(card_details!=False):
                print("\nThese are your saved card\n")
                for i in range(0,len(card_details[0])):
                    print(str(i+1)+". Card No: "+str(card_details[0][i])+", valid till: "+card_details[1][i])
                
                choice=input("\nDo you want to choose from saved card? 'Y' or 'N':") #If user wants they can go back to payment or return to main menu
                if(choice.upper()=='Y'):
                    while(True):
                        option=input("\nSelect the card: ")
                        if((int(option)>=1 and int(option)<=i+1)==False):
                            print("\nInvalid Option,Choose again")
                        else:
                            break
                    
                    print("\nYour Card: ",card_details[0][int(option)-1])
                    print("Valid till: ",card_details[1][int(option)-1])
                    pin=input("Enter 4 digit pin: ")
                    pin=booking_preplan_validations.validatePin(pin) #in real life senario it will be validate with actual pin 
                    print("Successfull payment of rupees ",total_amount)
                    '''in real life scenario here money will be deducted from bank'''
                    return
                else:
                    print("\nEnter details of new card")
                        
            card_no=input("\nEnter Card Number: ")
            card_no=booking_preplan_validations.validateCardNumber(card_no)
            valid_till=input("Enter Expiry date (mm/yyyy): ")
            valid_till=booking_preplan_validations.validateCardExpiry(valid_till)
            pin=input("Enter 4 digit pin: ")
            pin=booking_preplan_validations.validatePin(pin)  #in real life senario it will be validate with actual pin
            
            print("Successfull payment of rupees ",total_amount)
            '''in real life scenario here money will be deducted from bank'''
            
            choice=input("\nDo you want to save this card? 'Y' or 'N':") #If user wants they can go back to payment or return to main menu
            if(choice.upper()=='Y'):
                booking_preplan_db.saveCardDetails(uid, card_no, valid_till) #saving the card details except pin no
                print("Your card details have been saved successfully")
        
        except booking_preplan_exceptions.CardAlreadySavedException as e:
            print(e)
        
        except booking_preplan_exceptions.SomethingWrongException as e:
            raise e
        
        except Exception as e:
            print(e)
            choice=input("\nDo you want to try again? 'Y' or 'N': ") #If user wants they can go back to payment or return to main menu
            if(choice.upper()=='Y'):
                Booking.payment(uid, total_amount) #If user wants they can go back to payment
            else:
                return False#return to main menu
            
            
            
    @staticmethod
    def showBooking(uid):
        try:
            print("\nPyadventure Booking Details\n")
            booking_details=booking_preplan_db.getBookingDetails(uid) #getting booking details
            if(booking_details==False):
                print("You don't have any booking details\n")
                return
        
            print("These are your booking")
            for i in range(0,len(booking_details[0])):
                    print("\nBooking "+str(i+1)+":")
                    print("booking Id: "+str(booking_details[0][i]))
                    print("Your Adventur: "+booking_details[1][i])
                    print("location: "+booking_details[2][i])
                    date=Booking.changeDateFormat(str(booking_details[3][i]))
                    print("Date: "+date)
                    print("Amount per person: ",+booking_details[4][i])
                    print("No of People: ",+booking_details[5][i])
                    print("Total Amount: "+str(booking_details[6][i]))
                    
            
            
            while(True):
                choice=input("\nDo you want to know in details of any of the booking? 'Y' or 'N': ")
                if(choice.upper()=='Y'): 
                    while(True):
                        print("\nSelect your option\n")
                        for i in range(0,len(booking_details[0])):
                            print(str(i+1)+". Booking "+str(i+1))
                        option=input("\nEnter your choice: ")
                        if((int(option)>=1 and int(option)<=i+1)==False):
                            print("\nInvalid Option,Choose again")
                        else:
                            break
                    bid=str(booking_details[0][int(option)-1])
                    people_details=booking_preplan_db.getPeopleDetails(uid, bid)
                    if(people_details==False):
                        raise Exception
                    print("\nYou have booked for these people\n")
                    for i in range(0,len(people_details[0])):
                        print("\nPerson "+str(i+1)+":")
                        print("Name: "+people_details[0][i])
                        print("Gender: "+people_details[1][i])
                        print("Age: "+str(people_details[2][i]))
                               
                else:
                    return 
            
        except Exception:
            raise booking_preplan_exceptions.SomethingWrongException
        
        
        
    def preplanbooking(self,date,no_of_people):
        try:
            print("\nYour Adventure: ",self.__name)
            print("Location: ",self.__place)
            print("Amount per person: ",self.__amount_per_person)
            print("Date: ",date)
            date=booking_preplan_validations.validateDate(date)
            print("No of people: ",no_of_people)
            no_of_slots_available=booking_preplan_db.getAvailaleSlots(self.__aid, self.__place, date)
            if(int(no_of_slots_available)==0):
                print("Sorry, No slots availble for that date")
                raise booking_preplan_exceptions.NotEnoughSlotException #if no slots available for given date raise exception
            print("Available Slots: ",no_of_slots_available)
            if(int(no_of_people)>int(no_of_slots_available)):
                raise booking_preplan_exceptions.NotEnoughSlotException #if no enough slots available for given date and no of people raise exception
            
            self.__date=date
            self.__no_of_slots=no_of_people
            self.__total_amount=int(no_of_people)*int(self.__amount_per_person)
            print("Total amount: ",self.__total_amount)
            choice=input("\nDo you want to book? 'Y' or 'N':") #If user wants they can go back to bookin or return to main menu
            if(choice.upper()=='Y'):
                self.finalBooking(no_of_people)
            else:
                return #return to main menu
            
        except booking_preplan_exceptions.NotEnoughSlotException:
            print("Sorry, we don't have enough space for choosen date")
            choice=input("\nDo you want to choose any other date or different number of slot? 'Y' or 'N':") #If user wants they can go back to bookin or return to main menu
            if(choice.upper()=='Y'):
                self.booking() #If user wants they can go back to booking
            else:
                return #return to main menu
            
        except Exception as e:
            raise e
