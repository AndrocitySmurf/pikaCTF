import mysql.connector

mydb = mysql.connector.connect(
user = "AndrewInk",
passwd = "Inf0rmat10N!",
host = "localhost",
auth_plugin = "mysql_native_password",
database = "pikasql"
)

mycursor = mydb.cursor()
sql = "INSERT INTO users1 (name, address) VALUES (%s, %s)"
val = ("pikachutest", "true")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")
