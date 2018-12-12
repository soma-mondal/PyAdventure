'''This module is used for database interaction for find_adventure functionality'''


from utility.db_connectivity import createConnection,createCursor #importing connetion functions


def getAdventures():
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT aid,name FROM adventure1 ORDER BY aid")
        aid=[]
        name=[]
        for c1,c2 in cur:
            aid.append(c1)
            name.append(c2)
        return [aid,name]
    
    except Exception as e:
        raise e
        #here in real life scenario a alert will be sent to developer team with exception e
    finally:
        cur.close()
        con.close()
        
        
def getDescription(aid):
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT description FROM adventure1 WHERE aid="+str(aid))
        description=None
        for col1 in cur:
            description=col1[0]
        return description
    
    except Exception as e:
        raise e
        #here in real life scenario a alert will be sent to developer team with exception e 
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
        for c1,c2 in cur:
            place.append(c1)
            price.append(c2)
        return [place,price]
    
    except Exception as e:
        raise e
        #here in real life scenario a alert will be sent to developer team with exception e 
    finally:
        cur.close()
        con.close()