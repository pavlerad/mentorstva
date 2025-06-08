import pymysql

connection = pymysql.connect(host = "localhost",
                             user = "root",
                             password = "Djilkosh123",
                             database = "python17"





)

print(connection)


if connection.open == True:
    print('Connected')
else:
    print("Not connected")

input("\nPress 'Enter' key to exit.\n")


cursor = connection.cursor()

connection.commit()


def create_user(con, username, password, age):
    cursor = con.cursor()
    query = "INSERT INTO users (username, password, age) VALUES (%s , %s, %s)"
    cursor.execute(query, ("Yopa", "urlam55", 28))
    connection.commit()

create_user(connection, 'Pavle', 'Python250', 25)


cursor.close()
