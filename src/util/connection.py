import mysql.connector

USR = 'guilherme'
PASSWD = '3141'


def select_data(query):
    mydb = mysql.connector.connect(
        host='localhost',
        USR=USR,
        passwd=PASSWD,
        database=USR
    )

    def get_data():
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        return result

    return get_data()


def insert_data(query):
    mydb = mysql.connector.connect(
        host="localhost",
        USR=USR,
        passwd=PASSWD,
        database="USR"
    )

    def get_data():
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        mydb.commit()
        print(my_cursor.rowcount, "inserted.")

    return get_data()


def remove_data(query):
    mydb = mysql.connector.connect(
        host="localhost",
        USR=USR,
        passwd=PASSWD,
        database="USR"
    )

    def get_data():
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        mydb.commit()
        print(my_cursor.rowcount, "USR deleted.")

    return get_data()
