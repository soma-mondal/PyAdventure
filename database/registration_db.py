'''This module is used for database interaction for registration functionality'''


from utility.db_connectivity import createConnection,createCursor #importing connetion functions
from exceptions import registration_exceptions #importing user defined exceptions
import mysql.connector #importing mysql connector to get error object in exceptions


def userRegistration(user): #fuction to perform insertion of user information into database
    try:
        con=createConnection() #creating connection with database using db_connectivity module
        cur=createCursor(con) #creating cursor with database using db_connectivity module
        cur.execute("INSERT INTO USER(name,emailid,dateofbirth,contact_no,password,sec_qn,sec_ans) VALUES ('"+user.get_name()+"','"+user.get_emailid()+"','"+user.get_dateofbirth()+"','"+str(user.get_contact_no())+"','"+user.get_password()+"','"+user.get_sec_qn()+"','"+user.get_sec_ans()+"')");
        '''Inserting user data into databse'''
        cur.execute("SELECT uid FROM user WHERE emailid='"+user.get_emailid()+"'")
        '''Getting the user id of user'''
        uid=None
        for col1 in cur:
            uid=col1[0]
        user.set_uid(uid) #Setting the user id into user object
        con.commit()
        return user #returning user objects
    
    except mysql.connector.Error as e:
        if e.errno==1062: #It is the error mysql throw if email id is already present
            raise registration_exceptions.EmailAlreadyPresentException
        else:
            #here in real life scenario a alert will be sent to developer team with exception e
            raise registration_exceptions.SomethingWrongException 
        
    except Exception:
        #here in real life scenario a alert will be sent to developer team with exception e
        raise registration_exceptions.SomethingWrongException
         
    finally:
        cur.close()
        con.close()

