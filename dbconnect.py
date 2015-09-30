import MySQLdb 
import defs

def connection():
    conn=MySQLdb.connect(host = defs.HOST,
                         user = defs.USER,
                         passwd = defs.PASSWORD,
                         db = defs.DBASE)
    c=conn.cursor()
    
    return c,conn
