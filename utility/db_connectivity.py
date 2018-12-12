'''This module will be used to connect with DB and creating cursor'''


import mysql.connector


def createConnection(): #connectiong with the desire database
    return mysql.connector.connect(host='localhost', database='pyadventure', user='root', password='1234', buffered=True)
    
    
def createCursor(con): #cursor creating for 'con' connection
    return con.cursor()