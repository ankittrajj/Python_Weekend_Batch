#data base connect
# make a database
#make table in database
# ask user
# 1 name
# 2 age
# 3 amount
# 4 phone
# 5 address
# print account open



import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd='Ankit@8285',
                database='bankwe')

cursor = con.cursor()

while True:
    print("Bank Management System\n")
    choice = input("1. Open Account\n2.Cash Deposit\n3.Cash Withdrawl\n4.Update Acc\n5.Account Details\n6.Exit")
    # open account
    if choice == '1':
        name = input("Enter the customer name")
        amt = int(input("Enter the amount"))
        age = int(input("Enter the age"))
        phone = int(input("Enter the phone number"))

        query = "Insert into cust value('{}',{},{},{})".format(name,amt,age,phone)
        cursor.execute(query)
        con.commit()
        print('Account Opened!!')

    elif choice == '2':
        name = input('Enter the name of acc:-')
        amt = int(input("Enter the amt to deposit:-"))
        query = "update cust set amount={} where name='{}'".format(amt,name)
        cursor.execute(query)
        con.commit()
        print("Amount Deposit")


    #   exit
    elif choice =='6':
        break;