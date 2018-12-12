'''This module is used for database interaction for admin_menu functionality'''


from utility.db_connectivity import createConnection,createCursor #importing connetion functions
from exceptions import admin_menu_exceptions #importing user defined exceptions


def getMaxaid():
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT max(aid) FROM adventure1")
        aid=None
        for col1 in cur:
            aid=col1[0]
        return aid
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise admin_menu_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
        
def getAdventures():
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT aid,name FROM adventure1 ORDER BY aid")
        aid=[]
        name=[]
        for col1,col2 in cur:
            aid.append(col1)
            name.append(col2)
        return [aid,name]
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise admin_menu_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
        
def getAdventureDetails(aid):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT place,price FROM adventure2 WHERE aid="+str(aid))
        place=[]
        price=[]
        for col1,col2 in cur:
            place.append(col1)
            price.append(col2)
        return [place,price]
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise admin_menu_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()        


def addAdventure(adventure1,details):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("INSERT into adventure1 VAlUES("+str(adventure1.get_aid())+",'"+adventure1.get_name()+"','"+adventure1.get_description()+"')")
        '''Inserting data into adventure1 table'''
        cur.close()
        
        for adventure2 in details:
            cur=createCursor(con) #creating cursor with database using db_connectivity module
            cur.execute("INSERT into adventure2 VAlUES("+str(adventure2.get_aid())+",'"+adventure2.get_place()+"',"+str(adventure2.get_price())+","+str(adventure2.get_no_of_slots())+")")
            cur.close()
            
        con.commit()
        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise admin_menu_exceptions.SomethingWrongException
         
    finally:
        con.close()

        
def addLocation(details):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        for adventure2 in details:
            cur=createCursor(con) #creating cursor with database using db_connectivity module
            cur.execute("INSERT into adventure2 VAlUES("+str(adventure2.get_aid())+",'"+adventure2.get_place()+"',"+str(adventure2.get_price())+","+str(adventure2.get_no_of_slots())+")")
            cur.close()
            
        con.commit()
        
        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise admin_menu_exceptions.SomethingWrongException
         
    finally:
        con.close()
        
                
def editAdventureName(aid,name):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module    
        cur.execute("UPDATE adventure1 SET name='"+name+"' WHERE aid="+str(aid))
        con.commit()
        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise admin_menu_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
                
def editAdventureDescription(aid,description):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module    
        cur.execute("UPDATE adventure1 SET description='"+description+"' WHERE aid="+str(aid))
        con.commit()
        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise admin_menu_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        

def editLocationName(aid,place,new_place):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module    
        cur.execute("UPDATE adventure2 SET place='"+new_place+"' WHERE aid="+str(aid)+" AND place='"+place+"'")
        con.commit()
        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise admin_menu_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
        
def editPrice(aid,place,price):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module    
        cur.execute("UPDATE adventure2 SET price='"+str(price)+"' WHERE aid="+str(aid)+" AND place='"+place+"'")
        con.commit()
        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise admin_menu_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()


def editSlot(aid,place,no_of_slots):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module    
        cur.execute("UPDATE adventure2 SET no_of_slots='"+str(no_of_slots)+"' WHERE aid="+str(aid)+" AND place='"+place+"'")
        con.commit()
        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise admin_menu_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()       


def deleteAdventure(aid):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module    
        cur.execute("DELETE FROM adventure2 WHERE aid="+str(aid))
        cur.execute("DELETE FROM adventure1 WHERE aid="+str(aid))
        con.commit()
        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise admin_menu_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
        
def deleteAdventureLocation(aid,place):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module    
        cur.execute("DELETE FROM adventure2 WHERE aid="+str(aid)+" AND place='"+place+"'")        
        con.commit()
        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise admin_menu_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()