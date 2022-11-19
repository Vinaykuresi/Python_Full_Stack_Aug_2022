
import mysql.connector
from mysql.connector import Error

def iter_row(cursor, size):

    while True:
        rows = cursor.fetchmany(size)

        if not rows : 
            break

        for row in rows : 
            yield row

def connect():

    conn = None

    try : 
        conn = mysql.connector.connect(host = "localhost",
                                       database = "School",
                                       user = "root",
                                       password = "root")

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select * from Student")

            student_data = cursor.fetchall()

            ece_students = []

            for student_details in student_data : 
                if "ECE" in student_details:
                    ece_students.append(student_details)

            for ece_student in ece_students:
                print(ece_student)
                print()

            '''
            fetchone
            row = cursor.fetchone()

            while row is not None : 
                # continous iteration through table
                print(row)
                row = cursor.fetchone()
            '''

            '''
            fetchall
            # rows = cursor.fetchall()

            # print("Total Rows : ", cursor.rowcount)

            # for row in rows : 
            #     print(row)
            '''

            '''
            # fetchmany

            # for row in iter_row(cursor, 2):
            #     print(row)
            '''


    except Error as e : 
        print("The database error : ", e)

    finally : 

        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    connect()