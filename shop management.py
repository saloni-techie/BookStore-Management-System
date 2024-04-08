import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2111",
  database="example"
)

mycursor = mydb.cursor()

print("-------------------------------------------------Welcome To The BookStore---------------------------------------------")
print("Please Enter Your Name: \n")
name=input()
print("\nPlease Enter Your Phone Number: \n")
ph=int(input())
cart=[]
total=0

while(True):
    
    print("Choose \n 1.Customer \n 2.Store Keeper \n 3.Exit")
    choice=int(input())
    
    if(choice==1):
        while(True):
            print("\n\n Please Enter The Type Of Book You Want To Buy: \n 1.Textbook \n 2.References \n 3.General Knowledge \n 4.Others\n 5.Exit \n\n\n\n")
            tob=int(input())
            available=[]
            
            if(tob==1):
                sid="textbook"
            elif(tob==2):
                sid="reference"
            elif(tob==3):
                sid="gk"
            elif(tob==4):
                sid="others"
            elif(tob==5):
                exit()
            else:
                print("Wrong Choice")
                
            if(tob>=1 and tob<=4):
                print("Books Available In "+sid+" Section: \n\n")
                mycursor.execute("SELECT * FROM "+sid+"")
                myresult = mycursor.fetchall()
                print("SERIAL NO.".ljust(20),'BOOKNAME'.ljust(45),"AUTHOR".ljust(45),"PRICE".ljust(45),"QUANTITY".ljust(45))
                print()
                for x in myresult:
                    if(x[4]!=0):
                        print(str(x[0]).ljust(20),x[1].ljust(45),x[2].ljust(45),str(x[3]).ljust(45),str(x[4]).ljust(45))
                        available.append(x[0])


                n=int(input("enter srlno. of book you need: "))
                while(n not in available):
                    print("Wrong Serial No. Entered")
                    n=int(input("enter srlno. of book you need: "))
                    
                qty=int(input("Enter The No Of Book's You Want To Buy: "))

                    
                mycursor.execute("SELECT qty,name,price FROM "+sid+" where slno=%d"%(n))
                r=mycursor.fetchall()
                num=r[0][0]
                price=r[0][2]
                if(qty>num):
                     print("Sorry "+str(qty)+" Books Are Not Available.")
                     qty=int(input("Enter The No Of Book's You Want To Buy: "))
                     
                if(qty<=num):
                    cart.append([r[0][1],qty,num,price])
                    total=total+(price*qty)
                    sql = "UPDATE "+sid+" SET qty = "+str(num-qty)+" WHERE slno = "+str(n)+""
                    mycursor.execute(sql)
                    mydb.commit()
                        

                    print("\n Enter: \n1.To Show Invoice\n2.To Exit")
                    qq=input()

                    if qq=='1':
                        print("------INVOICE------\n\n")
                        print("Your Name :",name)
                        print("Your Number :\n",ph)
                        print()
                        print("BOOK NAME".ljust(30),'QUANTITY'.ljust(10),"PRICE".ljust(10),"TOTAL".ljust(15))
                        for i in cart:
                            print(i[0].ljust(30),str(i[1]).ljust(10),str(i[3]).ljust(10),str(i[1]*i[3]).ljust(15))
                        print("Net Total Amount: ",total,"\n")
                        print("Press any key to Exit or Enter to continue:")
                        if(input()):
                            s="INSERT INTO sales (name,total) VALUES (%s,%s)"
                            v=(name,str(total))
                            mycursor.execute(s,v)
                            mydb.commit()
                            
                            exit()
                    else:
                        s="INSERT INTO sales (name,total) VALUES (%s,%s)"
                        v=(name,str(total))
                        mycursor.execute(s,v)
                        mydb.commit()
                            
                        exit()
                else:
                   print("Sorry "+str(qty)+" Books Are Not Available.")
                   
    elif(choice==2):
        
        while(True):
            print("Choose\n 0.Add Book \n 1.Change Quantity \n 2.Change Price \n 3.Check Quantity \n 4.Sales Report \n 5.Exit")
            option=int(input())
            
            if(option==0):
                print("\n\n Please Enter The Type Of Book You Want To Add: \n 1.Textbook \n 2.References \n 3.General Knowledge \n 4.Others\n 5.Exit \n\n\n\n")
                tob=int(input())
                available=[]
                
                if(tob==1):
                    sid="textbook"
                elif(tob==2):
                    sid="reference"
                elif(tob==3):
                    sid="gk"
                elif(tob==4):
                    sid="others"
                elif(tob==5):
                    exit()
                else:
                    print("Wrong Choice")
                
                if(tob>=1 and tob <=4):
                    mycursor.execute("select max(slno) from textbook")
                    sl=mycursor.fetchall()
                    sl2=[lis[0] for lis in sl]
                    print("Serial no. upto ",sl2[0]," has been acquired ")
                    print("Please provide a new serial no. to it ")
                    sl=int(input("Enter The Serial No : "))
                    nm=input("Enter The Name Of The Book : ")
                    au=input("Enter The Name Of The Author : ")
                    p=int(input("Enter The Price Of The Book : "))
                    q=int(input("Enter The Quantity Of The Book : "))
                    
                    s="INSERT INTO "+sid+" (slno,name,author,price,qty) VALUES (%s,%s,%s,%s,%s)"
                    v=(str(sl),nm,au,str(p),str(q))
                    mycursor.execute(s,v)
                    mydb.commit()   
                
                
            elif(option==1):
                print("\n\n Please Enter The Type Of Book You Want To Change Its Quantity: \n 1.Textbook \n 2.References \n 3.General Knowledge \n 4.Others\n 5.Exit \n\n\n\n")
                tob=int(input())
                available=[]
                
                if(tob==1):
                    sid="textbook"
                elif(tob==2):
                    sid="reference"
                elif(tob==3):
                    sid="gk"
                elif(tob==4):
                    sid="others"
                elif(tob==5):
                    exit()
                else:
                    print("Wrong Choice")
                if(tob>=1 and tob<=4):
                    print("Books Available In "+sid+" Section: \n\n")
                    mycursor.execute("SELECT * FROM "+sid+"")
                    myresult = mycursor.fetchall()
                    print("SERIAL NO.".ljust(15),'BOOKNAME'.ljust(40),"AUTHOR".ljust(25),"PRICE".ljust(25),"QUANTITY".ljust(25))
                    print()
                    for x in myresult:
                        print(str(x[0]).ljust(15),x[1].ljust(40),x[2].ljust(25),str(x[3]).ljust(25),str(x[4]).ljust(25))
                        available.append(x[0])


                n=int(input("enter srlno. of book you want to add: "))
                while(n not in available):
                    print("Wrong Serial No. Entered")
                    n=int(input("enter srlno. of book you want to add: "))
                    
                qty=int(input("Enter The No Of Book's You Want To Add: "))

                    
                mycursor.execute("SELECT qty FROM "+sid+" where slno=%d"%(n))
                r=mycursor.fetchall()
                num=r[0][0]
                sql = "UPDATE "+sid+" SET qty = "+str(num+qty)+" WHERE slno = "+str(n)+""
                mycursor.execute(sql)
                mydb.commit()
                print()
                     
            elif(option==2):
                print("\n\n Please Enter The Type Of Book You Want To Change Its Price: \n 1.Textbook \n 2.References \n 3.General Knowledge \n 4.Others\n 5.Exit \n\n\n\n")
                tob=int(input())
                avail=[]
                
                if(tob==1):
                    sid="textbook"
                elif(tob==2):
                    sid="reference"
                elif(tob==3):
                    sid="gk"
                elif(tob==4):
                    sid="others"
                elif(tob==5):
                    exit()
                else:
                    print("Wrong Choice")
                if(tob>=1 and tob<=4):
                    print("Books Available In "+sid+" Section: \n\n")
                    mycursor.execute("SELECT * FROM "+sid+"")
                    myresult = mycursor.fetchall()
                    print("SERIAL NO.".ljust(15),'BOOKNAME'.ljust(40),"AUTHOR".ljust(25),"PRICE".ljust(15),"QUANTITY".ljust(15))
                    print()
                    for x in myresult:
                        print(str(x[0]).ljust(15),x[1].ljust(40),x[2].ljust(25),str(x[3]).ljust(15),str(x[4]).ljust(15))
                        avail.append(x[0])
                    print(avail)


                n=int(input("enter srlno. of book you want to change its price: "))
                while(n not in avail):
                    print("Wrong Serial No. Entered")
                    n=int(input("enter srlno. of book you want to change its price: "))
                    
                qty=int(input("Enter The New Price: "))

                sql = "UPDATE "+sid+" SET price = "+str(qty)+" WHERE slno = "+str(n)+""
                mycursor.execute(sql)
                mydb.commit()
                print()
                       
            elif(option==3):
                print("\n\n Please Enter The Type Of Book You Want To Check Quantity: \n 1.Textbook \n 2.References \n 3.General Knowledge \n 4.Others\n 5.Exit \n\n\n\n")
                tob=int(input())
                available=[]
                
                if(tob==1):
                    sid="textbook"
                elif(tob==2):
                    sid="reference"
                elif(tob==3):
                    sid="gk"
                elif(tob==4):
                    sid="others"
                elif(tob==5):
                    exit()
                else:
                    print("Wrong Choice")
                if(tob>=1 and tob<=4):
                    print("Books Available In "+sid+" Section: \n\n")
                    mycursor.execute("SELECT slno,name,qty FROM "+sid+"")
                    myresult = mycursor.fetchall()
                    print("SERIAL NO.".ljust(15),'BOOKNAME'.ljust(20),"QUANTITY".ljust(15))
                    print()
                    for x in myresult:
                        print(str(x[0]).ljust(15),x[1].ljust(20),str(x[2]).ljust(15))
                print()
        
            elif(option==4):
                mycursor.execute("SELECT * from sales")
                myresult = mycursor.fetchall()
                print("CUSTOMER NAME".ljust(20),'TOTAL AMOUNT'.ljust(20))
                print()
                for x in myresult:
                    print(x[0].ljust(20),str(x[1]).ljust(20))
                print()
                
            elif(option==5):
                exit()
                
            else:
                print("Wrong Input\n")
                
    elif(choice==3):
        
        exit()
        
    else:
        print("Wrong Input")
        
            

