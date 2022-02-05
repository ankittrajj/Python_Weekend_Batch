import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd='Ankit@8285',
                database = 'python_sql')

cursor = con.cursor()

while True:
    name = input("Enter the name")
    age=int(input("Enter the age"))
    marks=float(input("Enter the marks"))

    query = "Insert into student value('{}',{},{})".format(name,age,marks)
    cursor.execute(query)
    con.commit()
    print('Data enter successfully!!')

    option = input("Press 1 for enter more data and press 2 for exit")
    if option == '2':
        break;





# if con.is_connected():
#     print("Connection Successfull.....")
# else:
#     print('Not connected')