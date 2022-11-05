
import mysql.connector 
from mysql.connector import Error 


def connect_mysql_database() : 

    conn = None 

    try:
        conn = mysql.connector.connect(host = "localhost", 
                                        database="school", 
                                        user="root", 
                                        password="root")

        if conn.is_connected:
            print("Connected to MySQL Successfully")

    except Error as e :
        print("Connection to MySQL Unsuccessfull")

    finally :
        if conn is not None and conn.is_connected:
            conn.close()

if __name__ == "__main__":
    connect_mysql_database()
