import pymysql

flag=0
9

class login:

 def __init__(self):
   self.a=pymysql.connect(host="localhost",user="root",password="****",db="project")
   print("db connected")
   
   #signup function
 def signup(self,username,password):
    q="insert into login values('{0}','{1}')".format(username,password)
    c=self.a.cursor()
    c.execute(q)
    print("executed")
    self.a.commit()
    self.a.close()
    
    #signup fuction
 def signin(self,username,password):
    q="select * from login where username=%s  and password=%s"
    c=self.a.cursor()
    c.execute(q,(username,password))
    self.result=c.fetchone()
    self.a.commit()
    if self.result:
        print("login succes")
        global flag 
        flag=1    
    else:
        print("invalid username or password")
        