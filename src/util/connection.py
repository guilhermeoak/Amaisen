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

    def getData():
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        return result

    return getData()


def insert_data(query):
    mydb = mysql.connector.connect(
        host="localhost",
        USR=USR,
        passwd=PASSWD,
        database="USR"
    )

    def getData():
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        mydb.commit()
        print(my_cursor.rowcount, "inserted.")

    return getData()


def remove_data(query):
    mydb = mysql.connector.connect(
        host="localhost",
        USR=USR,
        passwd=PASSWD,
        database="USR"
    )

    def getData():
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        mydb.commit()
        print(my_cursor.rowcount, "USR deleted.")

    return getData()
