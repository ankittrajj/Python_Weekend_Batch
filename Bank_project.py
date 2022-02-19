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
    choice = input("1. Open Account\n2.Cash Deposit\n3.Cash Withdrawl\n4.Account Details\n5.Exit")
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

    # cash deposit
    elif choice == '2':
        name = input('Enter the name of acc:-')
        deposit_amt = int(input("Enter the amt to deposit:-"))
        query = "update cust set amount={} where name='{}'".format(deposit_amt,name)
        cursor.execute(query)
        con.commit()
        print("Amount Deposit")

    # 3.cash withdrawl------> if amount>curramt---->print('insufficient balance')
    # 4. update ----> cash withdrwal + cash deposit------> remaining amt.

    # cash withdrawl
    # elif choice == '3':
    #     name = input('Enter the name of acc:-')
    #     with_amt = int(input("Enter the amt to withdraw:-"))
    #     # deposit_amt =amount
    #     if with_amt>deposit_amt:
    #         print("Insufficient Balance")
    #     else:
    #         # print("Amount Withdrwal")
    #         query = "update cust set amount={} where name='{}'".format(with_amt,name)
    #         cursor.execute(query)
    #         con.commit()

    # 5 acc details
    elif choice=='4':
        name = input("Enter the acc name:-")
        query = "select * from cust where name='{}'".format(name)
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        con.commit()

    # exit
    elif choice =='5':
        break;


    # 1 bank sytem,hotel sytem,school management,hospital system.