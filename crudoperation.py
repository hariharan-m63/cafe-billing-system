import pymysql
class crud:
    def __init__(self):
         self.a=pymysql.connect(host="localhost",user="root",password="****",db="project")
         
         #add products in menu
    def add(self,product_id,product_name,price,quantity):
        q="insert into items values({0},'{1}',{2},{3})".format(product_id,product_name,price,quantity)
        c=self.a.cursor()
        c.execute(q)
        self.a.commit()
        
        #change quantity of products
    def updateqty(self,quantity,id):
         q="update items set quantity={0} where product_id ={1}".format(quantity,id)
         c=self.a.cursor()
         c.execute(q)
         self.a.commit() 
         
         #change price of products
    def updateprice(self,price,id):
         q="update items set price={0} where product_id ={1}".format(price,id)
         c=self.a.cursor()
         c.execute(q)
         self.a.commit() 
         
         #to see menu
    def view(self):
        q="select * from items"
        c=self.a.cursor()
        c.execute(q)
        print("id","item","price","stock")
        print("------------------ ")
        for p_id ,name, price, stock in c:
         print(p_id,name, price, stock)
        