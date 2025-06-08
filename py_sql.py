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
cursor.execute(("UPDATE users SET password = 'Remco123' WHERE id = 1"))
connection.commit()


def create_user(username, password, age):
    cursor = connection.cursor()
    cursor.execute(("INSERT INTO users (username, password, age) VALUES ('Pavle', 'Python250', 25)"))
    connection.commit()

create_user('Pavle','Python250', 25)
