'''This module is used for DB interaction for find_adventure functionality'''


from utility.db_connectivity import createConnection,createCursor #importing connetion functions
from exceptions import login_password_exceptions #importing user defined exceptions


def getPassword(emailid): #function to get password
    
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT uid,name,password FROM user WHERE emailid='"+emailid+"'") #geting the information of given emailid
        uid=None
        name=None
        password=None
        for c1,c2,c3 in cur:
            uid=c1
            name=c2
            password=c3
        return [uid,name,password] #returning those information
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise login_password_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()


def getAdminPassword(emailid): #function to get admin password
    
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT uid,name,password FROM user WHERE emailid='"+emailid+"' AND role='Admin'") #geting the admin information of given emailid
        
        uid=None
        name=None
        password=None
        for c1,c2,c3 in cur:
            uid=c1
            name=c2
            password=c3
        return [uid,name,password] #returning those information
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise login_password_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()


def getSecurityQuestionAnswer(emailid): #function to get security question, answer
    
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("SELECT uid,name,sec_qn,sec_ans FROM user WHERE emailid='"+emailid+"'") #getting the security question answer related information of given email id
        uid=None
        name=None
        sec_qn=None
        sec_ans=None
        for c1,c2,c3,c4 in cur:
            uid=c1
            name=c2
            sec_qn=c3
            sec_ans=c4
        return [uid,name,sec_qn,sec_ans] #returning those information
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise login_password_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()
        
        
def updatePassword(uid,password,sec_qn,sec_ans): #function to uodate password
    
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("UPDATE user SET password = '"+password+"', sec_qn='"+sec_qn+"', sec_ans='"+sec_ans+"' WHERE uid="+str(uid)) #updation new password,security question answer to database
        con.commit()
    
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise login_password_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()