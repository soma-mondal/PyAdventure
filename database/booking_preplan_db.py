'''This module is used for database interaction for bookin,preplan functionality'''


from utility.db_connectivity import createConnection,createCursor #importing connetion functions
from exceptions import booking_preplan_exceptions #importing user defined exceptions
import mysql.connector


def getAvailaleSlots(aid,place,date):    
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT no_of_slots FROM adventure2 WHERE aid="+str(aid)+" AND place='"+place+"'")
        total_slot=None
        for col1 in cur:
            total_slot=col1[0]
                             
        cur.execute("SELECT sum(no_of_slots) FROM booking WHERE date='"+date+"' AND aid="+str(aid)+" AND place='"+place+"'")
        booked_slot=None
        for col1 in cur:
            booked_slot=col1[0]
        if(booked_slot==None):
            return total_slot
        return int(total_slot)-int(booked_slot)
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise booking_preplan_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
        
def finalBooking(booking,people_information):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("INSERT INTO booking(uid,aid,name,place,date,amount_per_person,no_of_slots,total_amount) VALUES ('"+str(booking.get_uid())+"','"+str(booking.get_aid())+"','"+booking.get_name()+"','"+booking.get_place()+"','"+booking.get_date()+"','"+str(booking.get_amount_per_person())+"','"+str(booking.get_no_of_slots())+"','"+str(booking.get_total_amount())+"')");
        '''Inserting booking data into databse'''
        
        cur.execute("SELECT max(bid) FROM booking")
        '''Getting the booking id'''
        uid=booking.get_uid()
        bid=None
        for col1 in cur:
            bid=col1[0]
        booking.set_bid(bid) #Setting the bookingbooking id into  object
        cur.close()
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        for i in people_information:
            cur.execute("INSERT INTO people_information VALUES("+str(uid)+","+str(bid)+",'"+i[0]+"','"+i[1]+"',"+str(i[2])+")")
        con.commit()
        return booking #returning booking objects

        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise booking_preplan_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
def savePreplan(preplan):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("INSERT INTO preplan(uid,aid,name,place,date,amount_per_person,no_of_slots,total_amount) VALUES ('"+str(preplan.get_uid())+"','"+str(preplan.get_aid())+"','"+preplan.get_name()+"','"+preplan.get_place()+"','"+preplan.get_date()+"','"+str(preplan.get_amount_per_person())+"','"+str(preplan.get_no_of_slots())+"','"+str(preplan.get_total_amount())+"')");
        '''Inserting plan data into databse'''
        con.commit()
        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise booking_preplan_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
        
def getCardDetails(uid):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT card_no,valid_till FROM card WHERE uid="+str(uid))
        card_no=[]
        valid_till=[]
        for c1,c2 in cur:
            card_no.append(c1)
            valid_till.append(c2)
        if(len(card_no)==0):
            return False
        return [card_no,valid_till]
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise booking_preplan_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
        
        
def saveCardDetails(uid,card_no,valid_till):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("INSERT INTO card VALUES("+str(uid)+","+str(card_no)+",'"+valid_till+"')")
        con.commit()
    
    except mysql.connector.Error as e:
        if e.errno==1062: #It is the error mysql throw if email id is already present
            raise booking_preplan_exceptions.CardAlreadySavedException
        else:
            #here in real life scenario a alert will be sent to developer team with exception e
            raise booking_preplan_exceptions.SomethingWrongException 
        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise booking_preplan_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
def getPreplanDetails(uid):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT pid,aid,name,place,date,amount_per_person,no_of_slots,total_amount FROM preplan WHERE uid="+str(uid))
        pid=[]
        aid=[]
        name=[]
        place=[]
        date=[]
        amount_per_person=[]
        no_of_slots=[]
        total_amount=[]
        for c1,c2,c3,c4,c5,c6,c7,c8 in cur:
            pid.append(c1)
            aid.append(c2)
            name.append(c3)
            place.append(c4)
            date.append(c5)
            amount_per_person.append(c6)
            no_of_slots.append(c7)
            total_amount.append(c8)
        if(len(aid)==0):
            return False
        return [pid,aid,name,place,date,amount_per_person,no_of_slots,total_amount]
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise booking_preplan_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
def getBookingDetails(uid):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT bid,name,place,date,amount_per_person,no_of_slots,total_amount FROM booking WHERE uid="+str(uid))
        bid=[]
        name=[]
        place=[]
        date=[]
        amount_per_person=[]
        no_of_slots=[]
        total_amount=[]
        for c1,c2,c3,c4,c5,c6,c7 in cur:
            bid.append(c1)
            name.append(c2)
            place.append(c3)
            date.append(c4)
            amount_per_person.append(c5)
            no_of_slots.append(c6)
            total_amount.append(c7)
        if(len(bid)==0):
            return False
        return [bid,name,place,date,amount_per_person,no_of_slots,total_amount]
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise booking_preplan_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
        
def getPeopleDetails(uid,bid):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT name,gender,age FROM people_information WHERE uid="+str(uid)+" AND bid="+str(bid))
        name=[]
        gendar=[]
        age=[]
        
        for c1,c2,c3 in cur:
            name.append(c1)
            gendar.append(c2)
            age.append(c3)

        if(len(name)==0):
            return False
        
        return [name,gendar,age]
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise booking_preplan_exceptions.SomethingWrongException
    
    finally:
        cur.close()
        con.close()
    
def deletePreplan(pid):     
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("DELETE FROM preplan WHERE pid="+str(pid))
        con.commit()
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise booking_preplan_exceptions.SomethingWrongException
    
    finally:
        cur.close()
        con.close()