import mysql.connector
import db_settings as db

mydb = mysql.connector.connect(
    host=db.HOST,
    user=db.USER,
    passwd=db.PASSWD,
    database=db.DB
)


def select_data(query):
    def get_data():
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        return result

    return get_data()


def insert_data(query):
    def get_data():
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        mydb.commit()
        print(my_cursor.rowcount, "inserted.")

    return get_data()


def remove_data(query):
    def get_data():
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        mydb.commit()
        print(my_cursor.rowcount, "USER deleted.")

    return get_data()
