import mysql.connector


def setData(query):
    mydb = mysql.connector.connect(
        host='localhost',
        user='guilherme',
        passwd='3141',
        database='USER'
    )

    def getData():
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result

    return getData()


def insert_data(uery):
    mydb = mysql.connector.connect(
        host="localhost",
        user='guilherme',
        passwd='3141',
        database="USER"
    )

    def getData():
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()
        print(mycursor.rowcount, "user inserted.")

    return getData()


def remove_data(query):
    mydb = mysql.connector.connect(
        host="localhost",
        user='guilherme',
        passwd='3141',
        database="USER"
    )

    def getData():
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()
        print(mycursor.rowcount, "user deleted.")

    return getData()
