import mysql.connector

# Connection to database
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQL_wardwird0$",
    database="user"
)

# Login injectable
def login_checker_injectable(username, password):
    my_cursor = mydatabase.cursor()
    my_cursor.execute("SELECT * FROM user_authentication_2 WHERE username = '" + username + "' AND password = '" + password + "';")
    my_result = my_cursor.fetchall()
    print("Length of Query result: " + str(len(my_result)))
    if len(my_result) > 0:
        return True
    my_cursor.close()
