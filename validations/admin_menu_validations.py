'''This module is used to validate user given inputs in admin_menu module'''


from exceptions import admin_menu_exceptions


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
        raise admin_menu_exceptions.InvalidNameEmptyException #if empty throws exception
    if(len(name)>50):
        raise admin_menu_exceptions.InvalidNameLengthException #if more than 20 character throws exception 
    name_list=name.split()
    for i in name_list:
        if(i.isalpha()==False):
            raise admin_menu_exceptions.InvalidNameException #if contain any numeric throws exception
    return name


def validateDescription(description):  #validate the given name
    description=compress(description)
    if(description==""):
        raise admin_menu_exceptions.InvalidDescriptionEmptyException #if empty throws exception
    if(len(description)>500):
        raise admin_menu_exceptions.InvalidDescriptionLengthException #if more than 20 character throws exception 
    if(description.isdigit()==True):
        raise admin_menu_exceptions.InvalidDescriptionException #if description contain only digit throws exceptions
    return description


def validatePlace(place):  #validate the given name
    place=compress(place)
    if(place==""):
        raise admin_menu_exceptions.InvalidDescriptionEmptyException #if empty throws exception
    if(len(place)>50):
        raise admin_menu_exceptions.InvalidDescriptionLengthException #if more than 20 character throws exception 
    if(place.isdigit()==True):
        raise admin_menu_exceptions.InvalidPlaceException #if place contain only digit throws exceptions
    return place


def validatePrice(price): #validate the given price
    price=compress(price)
    if(price==""):
        raise admin_menu_exceptions.InvalidPriceEmptyException #must not empty else throws exception
    if(price.isdigit()==False):
        raise admin_menu_exceptions.InvalidPriceAlphabetException #can't contaion any alphabet else throws exception
    return price


def validateSlot(slot): #validate the given slot
    slot=compress(slot)
    if(slot==""):
        raise admin_menu_exceptions.InvalidSlotEmptyException #must not empty throws exception
    if(slot.isdigit()==False):
        raise admin_menu_exceptions.InvalidSlotAlphabetException #can't contaion any alphabet else throws exception
    return slot