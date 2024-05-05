import mysql.connector 
import datetime
import time
import sys
dis=[(1,'Football'),(2,'Vollyball'),(3,'Cricketbat'),(4,'Cricketball'), (5,'Tennisbat'),(6,'Tennisball'),  (7,'Badmracket'), (8,'Shutlecock'), (9,'Carrom')]
cost=[900,800,1000,300,1000,200,900,100,500]
def tprint(string):
    for i in range (len(string)):
        print(string[i],end='')
        time.sleep(0.0020)
    print()
def showmenu():
    print()
    print("Options")
    print("\t1. Add customer's detail")
    print("\t2. Show customer's bill")
    print("\t3. Delete customer's detail")
    print("\t4. Others")
    print("\t5. Exit")

def bill(lis):
    global cost, dis
    for l in lis:
        print("\t==========SPORT'S BILL ==============")
        print("\tBill.no:",l[0],"                                        ",l[2])
        print("\tCustomer's Name :",l[1])
        print("\tCustomer's Phone no. :",l[3])
        print("\t=====================================")
        print("\tProduct                         Qty          Price")
        print("\t=====================================")
        for i in range(4,len(l)-1):
            if l[i] == None:
                pass
            else:
                print('\t',dis[i-4][1],'               ',l[i],'           ',l[i]*cost[i-4])
        print("\t=====================================")
        print('\t Total                                                                ',l[13])
        print('\t======================================')

def create():
    global dis, cost
    dis_2=[]
    cost_1=[]
    ans=[] #to order
    items=[]#to order 
    total=0 
    prod=""
    prod_no=""

    date=str(datetime.datetime.now())[:10]
    name=str(input("\tenter customer's name: "))
    phone=int(input("\tenter customer's phone no. : "))
    print()
    tprint('\t====Menu=====')
    print('\t1.Football      ->$900')
    print('\t2.Vollyball     ->$800')
    print('\t3.Cricketbat   ->$1000')
    print('\t4.Cricketball   ->$300')
    print('\t5.Tennisball    ->$200')
    print('\t6.Tennisbat     ->$1000')
    print('\t7.Badminton racket->$900')
    print('\t8.Shuttlecock   ->$100')
    print('\t9.Carrom board->$500')
    print()
    while True:
        tprint('\tenter your product number from the option (enter 0 to close menu-entry)')
        try:
            pro=int(input('\t\t: '))
        except:
            print('\tenter no. from the above option only')
            print()
            continue
        if pro==0:
            break
        elif pro not in range(0,10):
            print('\tenter no. from the above option only')
            continue
        tprint('\tenter the number of product that you entered')
        try:
            pro_no=int(input('\t\t: '))
        except:
            print('\tenter only a number')
            print('\tenter again')
        print()
        cost_1.append((dis[pro-1][1],pro_no,(pro_no)*cost[pro-1]))#name , no, price
    for i in cost_1:
        itemname=i[0]
        count=0
        rupees=0
        if itemname not in items:
            for i in cost_1:
                if i[0]==itemname:
                    count+=i[1]
                    rupees+=i[2]
            ans.append((itemname,count,rupees))
        items.append(itemname)
    for i in range(len(ans)):
       prod += ans[i][0]+','
       prod_no += str(ans[i][1])+','
       total+=ans[i][2]
    prod=prod[:-1]
    prod_no=prod_no[:-1]
    #print(ans)
        
    cursor.execute("insert into sports_bill \
(Name, Ent_date, Phone_no, TotalCost,"+prod+") \
values ('"+name+"','"+date+"',"+str(phone)+", "+str(total)+", "+str(prod_no)+")")
    sql.commit()
    cursor.execute("select * from sports_bill where name = '"+name+"' and Phone_No='"+str(phone)+"' and Ent_date='"+str(date)+"'")
    billno=cursor.fetchall()
    #total=cursor.fetchall()[0][0]
    bill(billno)
    print()

def showbill():
    while True:
        print()
        name=str(input("\tenter customer's name: "))
        print()
        cursor.execute("select * from sports_bill where Name = '"+name+"'")
        fname=cursor.fetchall()
        if len(fname)>1:
            print('\tthere is '+str(len(fname))+' customers have same name. So,')
            date=str(input("\tenter the date of entry of customer: "))
            cursor.execute("select * from sports_bill where Name = '"+name+"' and Ent_date = '"+date+"'")
            fdate=cursor.fetchall()
            if len(fdate)>1:
                print("\tthere is "+str(len(fdate))+' customers have entered in the same date')
                billno=int(input("\tenter your bill no.: "))
                cursor.execute("select * from sports_bill where Name = '"+name+"' and Ent_date = '"+date+"' and BillNo = '"+str(billno)+"'")
                fbillno=cursor.fetchall()
                bill(fbillno)
                break
            elif len(fdate)==1:
                bill(fdate)
                break
            elif len(fdate)==0:
                print("\tthere is no customer's details entered in this date",date)
                print("\tTry Again")
                break
        elif len(fname)==1:
            bill(fname)
            break
        elif len(fname)==0:
            print('\tthere is no customer as name as ',name)
            print('\tTry Again')
            break

def deletebill():
    while True:
        print()
        name=str(input("\tenter customer's name: "))
        print()
        cursor.execute("select * from sports_bill where Name = '"+name+"'")
        fname=cursor.fetchall()
        if len(fname)>1:
            print('\tthere is '+str(len(fname))+' customers have same name. So,')
            date=str(input("\tenter the date of entry of customer: "))
            cursor.execute("select * from sports_bill where Name = '"+name+"' and Ent_date = '"+date+"'")
            fdate=cursor.fetchall()
            if len(fdate)>1:
                print("\tthere is "+str(len(fdate))+' customers have entered in the same date')
                billno=int(input("\tenter your bill no.: "))
                a=input("\tdo want to delete it (y/n): ")
                if a == 'y':
                    cursor.execute("delete from sports_bill where Name = '"+name+"' and Ent_date = '"+date+"' and BillNo = '"+str(billno)+"'")
                    sql.commit()
                    print('\tSucessfully deleted')
                break
            elif len(fdate)==1:
                print("\tCustomer's detail found")
                a=input("\tdo want to delete it (y/n): ")
                if a == 'y':
                    cursor.execute("delete from sports_bill where Name = '"+name+"' and Ent_date = '"+date+"'")
                    sql.commit()
                    print('\tSucessfully deleted')
                break
            elif len(fdate)==0:
                print("\tthere is no customer's details entered in this date",date)
                print("\tTry Again")
                break
        elif len(fname)==1:
            print("\tCustomer's detail found")
            a=input("\tdo want to delete it (y/n): ")
            if a == 'y':
                cursor.execute("delete from sports_bill where Name = '"+name+"'")
                sql.commit()
                print('\tSucessfully deleted')
            break
        elif len(fname)==0:
            print('\tthere is no customer as name as ',name)
            print('\tTry Again')
            break

def deleteall():
    con=input("\n\tDo you want to delete all the customer's details (y/n):")
    if con=='y':
        cursor.execute('delete from sports_bill')
        sql.commit()
        tprint('\n\tSucessfully Deleted')
def sum_total():
    cursor.execute('select sum(totalcost) from sports_bill')
    total=cursor.fetchall()[0][0]
    print('\n\tTotal cost of all customers =',total)
def average_total():
    cursor.execute('select avg(totalcost) from sports_bill')
    aveg=cursor.fetchall()[0][0]
    print('\n\tAverage of total cost of al customers =',aveg)    
   
#=================================================================================
sql=mysql.connector.connect(host="localhost",user="username",passwd="password")
cursor=sql.cursor()
cursor.execute("create database if not exists customer_details")
cursor.execute("use customer_details")
cursor.execute("create table if not exists sports_bill(\
    BillNo int not null primary key auto_increment,\
    Name varchar(20) not null,\
    Ent_date date,\
    Phone_No bigint(10),\
    Football int, Vollyball int, Cricketbat int, Cricketball int, Tennisbat int, Tennisball int, Badmracket int,\
    Shutlecock int, Carrom int,\
    TotalCost int)")

cursor.execute("alter table sports_bill auto_increment=12013000")
tprint('==============================================================')
tprint("====================SPORT'S BILLING SOFTWARE==================")
tprint('===============================================================')
while True:
    showmenu()
    tprint('\n\tChoose your option')
    try:
        choice=int(input('\t\t:'))
    except:
        print('\tenter no. from the option only ')
        print('\tTry Again')
        continue
    if choice == 1:
        create()
    elif choice == 2:
        showbill()
    elif choice == 3:
        deletebill()
    elif choice == 4:
        while True:
            print()
            tprint('\tselect your option')
            print("\n\t1.Total Cost of all customer's products")
            print("\t2.Average of total cost of all customer's products")
            print("\t3.Delete all customer's details")
            print("\t4.Back to the main option")
            try:
                choice=int(input('\t\t:'))
            except:
                print('\tenter no. from the option only ')
                print('\tTry Again')
                continue
            if choice == 1:
                sum_total()
            elif choice == 2:
                average_total()
            elif choice == 3:
                deleteall()
            elif choice == 4:
                break
    elif choice == 5:
        sys.exit()
