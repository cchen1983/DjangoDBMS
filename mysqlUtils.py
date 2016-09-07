import re
import os
import MySQLdb as sql

class dbContext:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        
        self.check_connection()

    def check_connection(self):
        try:
            con = sql.connect(user=self.user, passwd=self.password, host=self.host, db=self.database)
            con.close()
        except Exception,e:
            raise Exception('Problem connecting to the database.')

    def connect(self):
        return sql.connect(user=self.user, passwd=self.password, host=self.host, db=self.database)

EasyDriveContext = dbContext('root', 'root', 'localhost', 'EasyDriveProject')

def dbQuery(cmd):
    ctx = EasyDriveContext

    conn = ctx.connect()
    cursor = conn.cursor()

    res = None
    try:    
        print "User SQL command: " + cmd
        cursor.execute(cmd)
        tp = cursor.fetchall()
        if len(tp) > 0: 
            res = {'desc': [i[0] for i in cursor.description], 'tuples':tp}    
    except:
        res = None

    conn.close()

    return res

def dbExec(cmd):
    ctx = EasyDriveContext

    conn = ctx.connect()
    cursor = conn.cursor()
    res = True
    try:
        print "User SQL command: " + cmd
        cursor.execute(cmd)
        conn.commit()
    except:
        res = False
    
    conn.close()
    return res
