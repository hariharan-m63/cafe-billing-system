import loginpage
import crudoperation
import bill3
import reports

try:
        log=loginpage.login()
        print("1.signup\n2.signin\n")
        c=int(input("enter your choice:"))
        
        if c==1:
            user=input("enter user name :")
            password=input("enter password:")
            log.signup(user,password)
            
        elif c==2:
            user=input("enter user name :")
            password=input("enter password:")
            log.signin(user,password)
            
        if loginpage.flag==1:
            a=crudoperation.crud()
            while True: 
                print("\n\n3.add items\n4.update\n5.view menu\n6.bill\n7.report\n8.Exit\n")
                c=int(input("enter choice:"))
                
                if c==3:
                  id=input("id:")
                  name=input("name:")
                  price=input("price:")
                  quantity=input("quantity:")
                  a.add(id,name,price,quantity)
                  
                elif c==4:
                      print("4.1 update quantity\n4.2 update price\n")
                      upt=float(input("enter choice to update:"))
                      if upt==4.1:
                         qty=input("enter quantity:")
                         id=input("id:")
                         a.updateqty(qty,id)
                      elif upt==4.2:
                        price=input("price:")
                        id=input("id:")
                        a.updateprice(price,id)
                        
                elif c==5:
                     a.view()
                     
                elif c==6:
                    b=bill3.billing()
                    b.generate_bill()
                    
                elif c == 7:
                   r = reports.reports()
                   print("1. Daily Report\n2. Monthly Report")
                   ch = int(input("Enter choice: "))
                   if ch == 1:
                       r.daily_report()
                   elif ch == 2:
                       r.monthly_report()
                       
                elif c==8:
                    print("application closed")
                    break
               
except Exception as e:
    print(e)
        