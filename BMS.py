import mysql.connector
import pickle

mydb=mysql.connector.connect(user=’Vidhi Iyer’,
                             passwd='vidhi307331’,
                             host='localhost',
                             auth_plugin='mysql_native_password',
                             database='bank'
                             )

mycursor=mydb.cursor(buffered=True)


def Menu():
    print('*'*140)
    myfile=open(R"C:\Mukul's\Python\file1.txt","r")
    str=myfile.read()
    print(str)
    print('MAIN MENU')
    print('1. Insert record/records')
    print('2. Display recods as per Account no. ')
    print('  a. Sorted as per Account no.')
    print('  b. Sorted as per Customer name.')
    print('  c. Sorted as per Customer balance ')
    print('3. Search record details as per Account no.')
    print('4. Update record')
    print('5. Transaction-Debit/Withdraw from the account')
    print('  a. Debit/Withdraw from the account')
    print('  b. Credit into the account')
    print('6. EXIT')
    print('*'*140) 

def MenuSort():
     print('  a. Sorted as per Account no.'.center(140))
     print('  b. Sorted as per Customer name.'.center(140))
     print('  c. Sorted as per Customer balance '.center(140))
     print('  d. Back'.center(140))

def MenuTransaction():
     print('  a. Debit/Withdraw from the account'.center(140))
     print('  b. Credit into the account'.center(140))
     print('  c. Back'.center(140))

def Create():
    try:
        mycursor.execute('create table bank(ACCNO varchar(10), NAME varchar(20), MOBILE varchar(10), EMAIL varchar(25), ADDRESS varchar(25), CITY varchar(20), COUNTRY varchar(20), BALANCE float(20) )')
        print('TABLE CREATED')
        Insert()
    except:
        print('TABLE EXIST')
        Insert()

def Insert():
    while True:
        Acc=input("Enter Account number=")
        Name=input("Enter name=")
        Mob=input("Enter mobile no.=")
        email=input("Enter email=")
        Add=input("Enter address=")
        City=input("Enter city=")
        Country=input("Enter country=")
        Bal=float(input("Enter your balance="))
        Rec=[Acc,Name.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Bal]
        Cmd="insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd,Rec)
        mydb.commit()
        ch=input("Do you want to enter more records ?")
        if ch=='N' or ch=='n':
            break

def DispSortAcc():
    try:
        cmd="select * from bank order by ACCNO;"
        mycursor.execute(cmd)
        F="%15s,%15s,%15s,%15s,%15s,%15s,%15s,%15s"
        print(F%("ACCNO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s"%j, end='')
            print()
        print("="*125)
    except:
        print("Table doesn't exist")

def DispSortName():
    try:
        cmd="select * from bank order by NAME"
        mycursor.execute(cmd)
        F="%15s,%15s,%15s,%15s,%15s,%15s,%15s,%15s"
        print(F%("ACCNO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s"%j, end='')
            print()
        print("="*125)
    except:
        print("Table doesn't exist")

def DispSortBal():
    try:
        cmd="select * from bank order by BALANCE;"
        mycursor.execute(cmd)
        F="%15s,%15s,%15s,%15s,%15s,%15s,%15s,%15s"
        print(F%("ACCNO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s"%j, end='')
            print()
        print("="*125)
    except:
        print("Table doesn't exist")

def DispSearchAcc():
    try:
        cmd="select * from bank;"
        mycursor.execute(cmd)
        ch=input('Enter accno. to be searched')
        for i in mycursor:
            if i[0]==ch:
                print('='*125)
                F="%15s,%15s,%15s,%15s,%15s,%15s,%15s,%15s"
                print(F%("ACCNO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
                print("="*125)
                for j in i:
                    print("%14s"%j, end='')
                print()
                break
        else:
            print('Record not found')
    except:
        print("Table doesn't exist")

def Update():
    try:
        cmd="select * from bank;"
        mycursor.execute(cmd)
        A=input('ENTER THE ACCOUNT NO. WHOSE DETAILS ARE TO BE CHANGED')
        for i in mycursor:
            i=list(i)
            if i[0]==A:
                ch=input("Change Name(Y/N)")
                if ch=='y' or ch=='Y':
                    i[1]=input('Enter Name')
                    i[1]=i[1].upper()

                ch=input("Change Mobile(Y/N)")
                if ch=='y' or ch=='Y':
                    i[2]=input('Enter Mobile')
                    i[2]=i[2].upper()

                ch=input("Change Email(Y/N)")
                if ch=='y' or ch=='Y':
                    i[3]=input('Enter Email')
                    i[3]=i[3].upper()

                ch=input("Change Address(Y/N)")
                if ch=='y' or ch=='Y':
                    i[4]=input('Enter Address')
                    i[4]=i[4].upper()

                ch=input("Change City(Y/N)")
                if ch=='y' or ch=='Y':
                    i[5]=input('Enter City')
                    i[5]=i[5].upper()

                ch=input("Change Country(Y/N)")
                if ch=='y' or ch=='Y':
                    i[6]=input('Enter Country')
                    i[6]=i[6].upper()

                ch=input("Change Balance(Y/N)")
                if ch=='y' or ch=='Y':
                    i[7]=float(input('Enter Balance'))
                cmd="UPDATE bank SET NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s WHERE ACCNO=%s;"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Updated")
                break
            else:
                print("Oops.....Record not found")        
    except:
        print("No such table")


def Debit():
    cmd="select * from bank;"
    mycursor.execute(cmd)
    print("Please note that the money can only be Debited if minimum amount of Rs.5000 exists")
    acc=input("Enter the account no. from which the money is to be debited:-")
    for i in mycursor:
        i=list(i)
        if i[0]==acc:
            Amt=float(input("Enter amount to be withdrawn:"))
            if i[7]-Amt>=5000:
                i[7]-=Amt
                cmd="UPDATE bank SET BALANCE=%s WHERE ACCNO=%s;"
                val=(i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Amount Debited")
                break
            else:
                print("There must be a balance of Rs. 5000")
                break
        else:
            print("Record not found")
       
def Credit():
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        acc=input("Enter the account no. from which the money is to be credited:-")
        for i in mycursor:
            i=list(i)
            if i[0]==acc:
                Amt=float(input("Enter amount to be withdrawn"))                
                i[7]+=Amt
                cmd="UPDATE bank SET BALANCE=%s WHERE ACCNO=%s;"
                val=(i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Amount Credited")
                break
        else:
            print("Record not found")
    except:
        print("Table doesn't exist")


while True:
   Menu()
   ch=input("Enter your choice:")
   if ch=="1":
      Create()
   elif ch=="2":
       while True:
           MenuSort()
           ch1=input("Enter choices a/b/c/d:")
           if ch1 in ["a","A"]:
               DispSortAcc()
           elif ch1 in ['b','B']:
               DispSortName()
           elif ch1 in ['c','C']:
               DispSortBal()
           elif ch in ['d','D']:
               print("Back to main menu")
           break
       else:
           print('Invalid choice')
   elif ch=='3':
      DispSearchAcc()
   elif ch=='4':
      Update()
   elif ch=='5':
      while True:
         MenuTransaction()
         ch1=input("Enter choices a/b/c")
         if ch1 in ['a','A']:
            Debit()
         elif ch1 in ['b','B']:
            Credit()
         elif ch1 in ['c','C']:
            print("back to main menu")
            break
         else:
            print("Invalid choice")
   elif ch=='6':
      print("Exiting...")
      break
   else:
      print("Wrong choice entered")
