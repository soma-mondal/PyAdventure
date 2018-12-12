'''This is a module which contain all the class defination user in PyAdventure Application'''


class User: #User class is used when new user registration is done
    def __init__(self,name,emailid,dateofbirth,contact_no,password,sec_qn,sec_ans):
        self.__uid=None
        self.__name=name
        self.__emailid=emailid
        self.__dateofbirth=dateofbirth
        self.__contact_no=contact_no
        self.__password=password
        self.__sec_qn=sec_qn
        self.__sec_ans=sec_ans
        
    def get_uid(self):
        return self.__uid
    def get_name(self):
        return self.__name
    def get_emailid(self):
        return self.__emailid
    def get_dateofbirth(self):
        return self.__dateofbirth
    def get_contact_no(self):
        return self.__contact_no
    def get_password(self):
        return self.__password
    def get_sec_qn(self):
        return self.__sec_qn
    def get_sec_ans(self):
        return self.__sec_ans

    def set_uid(self, uid):
        self.__uid = uid


class Adventure1: #Adventure1 class is used when new adventure is added
    def __init__(self,aid,name,description):
        self.__aid=aid
        self.__name=name
        self.__description=description

    def get_aid(self):
        return self.__aid
    def get_name(self):
        return self.__name
    def get_description(self):
        return self.__description

    def set_aid(self, aid):
        self.__aid = aid


class Adventure2: #Adventure2 class is used when new location for an adventure is added
    def __init__(self,aid,place,price,no_of_slots):
        self.__aid=aid
        self.__place=place
        self.__price=price
        self.__no_of_slots=no_of_slots

    def get_aid(self):
        return self.__aid
    def get_place(self):
        return self.__place
    def get_price(self):
        return self.__price
    def get_no_of_slots(self):
        return self.__no_of_slots

    def set_aid(self, aid):
        self.__aid = aid