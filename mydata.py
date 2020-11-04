import mysql.connector


mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQL_wardwird0$",
    database="user"
)

my_cursor = mydatabase.cursor()


def login_checker(username, password):
    my_cursor.execute("SELECT * FROM user_authentication WHERE username = '" + username + "' AND password = '" + password + "';")
    myresult = my_cursor.fetchall()
    print(len(myresult))
    if len(myresult) > 0:
        return True


def login_checker_2(username, password):
    my_cursor.execute("SELECT * FROM user_authentication")
    myresult = my_cursor.fetchall()
    for data in myresult:
        for index in data:
            if index == username:
                pw = data[2]
                if password == pw:
                    return True
                else:
                    return False
