'''
Redirected from index.py, This module is for login a Admin and other admin Admin,
It verify user input using login_password_validations.py from validation package,
interact with database using login_password_db.py from database package,
and use user defined exceptions from login_password_exceptions.py from exception package
'''


from classes.pyadventure_class import Adventure1,Adventure2 #importing of Adventure1, Adventure2 class
from validations import login_password_validations,admin_menu_validations #importing validation module to validate user inputs
from exceptions import login_password_exceptions,admin_menu_exceptions #importing exception module to get user defined exceptions
from database import login_password_db,admin_menu_db #importing database module to interact with MySQL database
from functionality.password import Password #importing Password class to redirect to forgrtPassword funtion if account is locked


class Admin:
    @staticmethod
    def adminMenu(): #options for admin to choose
        print("\nPyAdventure Admin Menu: \n")
        while(True):
            print("1. Login")
            print("2. Change Password/Forget password")
            print("3. Exit")
            option=input("\nEnter your choice: ")
            if(option.isdigit() and int(option)>0 and int(option)<=3): #redirect accordingly
                if(int(option)==1):
                    Admin.adminLogin()
                    break
                elif(int(option)==2):
                    Password.passwordIssue()
                    break
                else:
                    return
            else:
                print("\nInvalid Choice. Choose again\n")
    
    
    @staticmethod
    def adminLogin():
        try:
            print("\nPyadventure Admin Login: \n")
            emailid=input("Enter your email id: ")
            emailid=login_password_validations.validateEmailIdSyntax(emailid)
            info=login_password_db.getAdminPassword(emailid)
            if(info[0]==None):
                raise login_password_exceptions.NotAdminException  #if not admin throes exception
            
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
                        raise login_password_exceptions.WrongPasswordException #if three times worng password throes exception
                    print("\nWrong Password. Please try again\n") 
                    count+=1
            name=info[1].split()[0]
            print("\nWelcome back "+name)
            while(True):
                print("\nChosse a option from below\n") #after successfull loging options for Admin
                print("1. Add/Edit/Delete Adventure")
                print("2. Logout")
                option=input("\nEnter your choice: ")
                if(option.isdigit() and int(option)>0 and int(option)<=2):
                    if(int(option)==1):
                        Admin.adminAddEditDelete()
                    else:
                        return
                else:
                    print("\nInvalid Choice. Choose again")
            
            
        except login_password_exceptions.NotAdminException as e:
            print(e) #if not admin redirect to main menu
            print("You can't login as Admin")
            return
        
        except login_password_exceptions.WrongPasswordException as e:
            print(e) #if wrong password redirect to forget password
            print("Your account has been locked\n") 
            print("We are redirecting you to Forget Password Protal, Kindly set a new password")
            Password.forgetPassword()
            
        except (login_password_exceptions.SomethingWrongException,admin_menu_exceptions.SomethingWrongException) as e:
            print(e)
            print("We are redirecting you to the main menu") #If any unexpected db error occur it will redirect to main menu
            return   
        
        except Exception as e:
            print(e)
            choice=input("\nDo you want to continue? 'Y' or 'N': ") #If user wants they can go back to admin login portal or return to main menu
            if(choice.upper()=='Y'):
                Admin.adminLogin()  #If user wants they can go back to admin login portal
            else:
                return  #return to main menu
                
                
    @staticmethod         
    def adminAddEditDelete():
        try:
            print("\nPyAdventure Admin Menu")
            while(True):
                print("\nSelect your choice\n")
                print("1. Add a new adventure")
                print("2. Add location of an old adventure ")
                print("3. Edit name of an adventure")
                print("4. Edit description of an adventure")
                print("5. Edit location name of an adventure")
                print("6. Edit price of an adventure")
                print("7. Edit slots of an adventure")
                print("8. Delete an adventure")
                print("9. Delete location of an adventure ")
                print("10. Exit")
                option=input("\nEnter your choice: ")
                if(option.isdigit() and int(option)>0 and int(option)<=10): #redirect accordingly
                    if(int(option)==1):
                        '''Start: add a new adventure'''
                        print("\nEnter the follwing to add an adventure")
                        name=input("\nEnter adventute name: ")
                        name=admin_menu_validations.validateName(name)
                        description=input("Enter description: ")
                        description=admin_menu_validations.validateDescription(description)
                        aid=admin_menu_db.getMaxaid()+1
                        adventure1=Adventure1(aid,name,description)
                        
                        flag=0
                        while(True):
                            count=input("\nHow many locations you want to add? Enter:")
                            if(count.isdigit()==False):
                                print("It must be a number")
                                continue
                            count=int(count)
                            if(count==0):
                                print("You must add at least one location")
                                choice=input("Do you want to exit? Y/N")
                                if(choice.upper()=='Y'):
                                    flag=1
                                    break
                                else:
                                    continue
                            break
                        
                        if(flag==1):
                            continue
                        
                        details=[]
                        while(count>0):
                            place=input("\nEnter Location:")
                            place=admin_menu_validations.validatePlace(place)
                            price=input("Enter price: ")
                            price=admin_menu_validations.validatePrice(price)
                            no_of_slots=input("Enter total number of slots: ")
                            no_of_slots=admin_menu_validations.validateSlot(no_of_slots)
                            adventure2=Adventure2(aid,place,price,no_of_slots)
                            details.append(adventure2)
                            count=count-1
                            
                        admin_menu_db.addAdventure(adventure1, details)
                        print("\nAdventure is added successfully")
                        '''END: add a new adventure''' 
                        
                    elif(int(option)==2):
                        '''Start: add location of an old adventure'''
                        print("\nChoose an option from below to add location. \n")
                        result=Admin.optionAdventure()
                        if(result==False):
                            continue
                        aid=result
                        
                        flag=0
                        while(True):
                            count=input("\nHow many locations you want to add? Enter:")
                            if(count.isdigit()==False):
                                print("It must be a number")
                                continue
                            count=int(count)
                            if(count==0):
                                print("You must add at least one location")
                                choice=input("Do you want to exit? Y/N")
                                if(choice.upper()=='Y'):
                                    flag=1
                                    break
                                else:
                                    continue
                            break
                        
                        if(flag==1):
                            continue
                        
                        details=[]
                        while(count>0):
                            place=input("\nEnter Location:")
                            place=admin_menu_validations.validatePlace(place)
                            price=input("Enter price: ")
                            price=admin_menu_validations.validatePrice(price)
                            no_of_slots=input("Enter total number of slots: ")
                            no_of_slots=admin_menu_validations.validateSlot(no_of_slots)
                            adventure2=Adventure2(aid,place,price,no_of_slots)
                            details.append(adventure2)
                            count=count-1
                            
                        admin_menu_db.addLocation(details)
                        print("\nLocation is added successfully")
                        '''End: add location of an old adventure'''
                        
                    elif(int(option)==3):
                        '''Start: edit name of an adventure'''
                        print("\nChoose an option from below to edit adventure name. \n")
                        result=Admin.optionAdventure()
                        if(result==False):
                            continue
                        aid=result
                        
                        name=input("\nEnter new name: ")
                        name=admin_menu_validations.validateName(name)
                        admin_menu_db.editAdventureName(aid, name)
                        print("\nAdventure name edited successfully")
                        '''End: edit name of an adventure'''
                        
                    elif(int(option)==4):
                        '''Start: edit description of an adventure'''
                        print("\nChoose an option from below to edit adventure description. \n")
                        result=Admin.optionAdventure()
                        if(result==False):
                            continue
                        aid=result
                        
                        description=input("\nEnter new description: ")
                        description=admin_menu_validations.validateDescription(description)
                        admin_menu_db.editAdventureDescription(aid, description)
                        print("\nAdventure description edited successfully")
                        '''End: edit description of an adventure'''
                        
                    elif(int(option)==5):
                        '''Start: edit location name of an adventure'''
                        print("\nChoose an option from below to edit location name of an adventure. \n")
                        result=Admin.optionAdventureLocation()
                        if(result==False):
                            continue
                        
                        aid=result[0]
                        place=result[1]
                                               
                        new_place=input("\nEnter new location name:")
                        new_place=admin_menu_validations.validatePlace(new_place)
                        admin_menu_db.editLocationName(aid, place, new_place)
                        print("\nlocation name is edited successfully")
                        '''End: edit location name of an adventure'''
                        
                    elif(int(option)==6):
                        '''Start: edit price of an adventure'''
                        print("\nChoose an option from below to edit price of an adventure. \n")
                        result=Admin.optionAdventureLocation()
                        if(result==False):
                            continue
                        
                        aid=result[0]
                        place=result[1]
                        
                        price=input("\nEnter new price: ")
                        price=admin_menu_validations.validatePrice(price)
                        admin_menu_db.editPrice(aid, place, price)
                        print("\nPrice is edited successfully")
                        '''End: edit price of an adventure'''
                        
                    elif(int(option)==7):
                        '''Start: edit slot of an adventure'''
                        print("\nChoose an option from below to edit slot of an adventure. \n")
                        result=Admin.optionAdventureLocation()
                        if(result==False):
                            continue
                        
                        aid=result[0]
                        place=result[1]
                        
                        no_of_slots=input("\nEnter new total number of slots: ")
                        no_of_slots=admin_menu_validations.validateSlot(no_of_slots)
                        admin_menu_db.editSlot(aid, place, no_of_slots)
                        print("\nSlots is edited successfully")
                        '''End: edit slot of an adventure'''
                        
                    elif(int(option)==8):
                        '''Start: delete an adventure'''
                        print("\nChoose an option from below to delete adventure. \n")
                        result=Admin.optionAdventure()
                        if(result==False):
                            continue
                        
                        admin_menu_db.deleteAdventure(aid)
                        print("\nAdventure deleted successfully")
                        '''End: delete an adventure'''
                    elif(int(option)==9):
                        '''Start: delete location of an adventure'''
                        print("\nChoose an option from below to delete location of an adventure. \n")
                        result=Admin.optionAdventureLocation()
                        if(result==False):
                            continue
                        
                        aid=result[0]
                        place=result[1]
                        
                        admin_menu_db.deleteAdventureLocation(aid, place)
                        print("\nLocation is deleted successfully")
                        '''End: delete location of an adventure'''
                        
                    else:
                        return
                else:
                    print("\nInvalid Choice. Choose again")
                    
        except admin_menu_exceptions.SomethingWrongException as e:
            raise e
          
        except Exception as e:
            print(e)
            choice=input("\nDo you want to continue? 'Y' or 'N': ") #If user wants they can go back to admin login portal or return to main menu
            if(choice.upper()=='Y'):
                Admin.adminAddEditDelete() #If user wants they can go back to admin login portal
            else:
                return  #return to main menu
            
            
    @staticmethod
    def optionAdventure(): #a module which will give user options as adventure name,user can select one 
        adventures=admin_menu_db.getAdventures()
        while(True):
            for i in range(0,len(adventures[0])):
                print(str(adventures[0][i])+". "+adventures[1][i])
            print("e. Exit")
            option=input("\nEnter your choice: ")
            if(option=='e'):
                return False
            if(int(option) not in adventures[0]):
                print("\nInvalid Option,Choose again\n")
            else:
                break
                                                    
        aid=int(option)
        name=adventures[1][aid-1]
        print("\nYou have choosen: ",name)
        return aid
    
    
    @staticmethod
    def optionAdventureLocation(): #a module which will give user options as adventure name and then locations, user can select one of each
        adventures=admin_menu_db.getAdventures()
        while(True):
            for i in range(0,len(adventures[0])):
                print(str(adventures[0][i])+". "+adventures[1][i])
            print("e. Exit")
            option=input("\nEnter your choice: ")
            if(option=='e'):
                return False
            if(int(option) not in adventures[0]):
                print("\nInvalid Option,Choose again\n")
            else:
                break
                                                    
        aid=int(option)
        name=adventures[1][aid-1]
        print("\nYou have choosen: ",name)
                        
        details=admin_menu_db.getAdventureDetails(aid)
        print("\nChoose an option from below to select location. \n")
                        
        while(True):
            for i in range(0,len(details[0])):
                print(str(i+1)+". "+details[0][i]+" - "+str(details[1][i]))
            print("e. Exit")
            option=input("\nSelect the place from given list or e for Exit: ")
            if(option=='e'):
                return False
            if((int(option)>=1 and int(option)<=i+1)==False):
                print("\nInvalid Option,Choose again\n")
            else:
                break
                            
        place=details[0][int(option)-1]
        print("\nYou have choosen: ",place) 
        return [aid,place]
    