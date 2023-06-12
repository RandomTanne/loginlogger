import os
import mysql.connector

userpass = os.getlogin()
db_connection = mysql.connector.connect(host="localhost", user=userpass, password=userpass)
cursor = db_connection.cursor()
useDBQuery = f"USE {userpass}"
cursor.execute(useDBQuery)
logToDBQuery = f"INSERT INTO {userpass} (timestamp, currentuser) VALUES(NOW(), '{str(userpass)}')"
cursor.execute(logToDBQuery)
db_connection.commit()
cursor.close()
db_connection.close()