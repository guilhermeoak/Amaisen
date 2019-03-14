import mysql.connector


def setData(query):
    mydb = mysql.connector.connect(
        host='localhost',
        user='user',
        passwd='1234',
        database='USER'
    )

    def getData():
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result

    return getData()


def insertData(user, passwd, query):
    mydb = mysql.connector.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        database="USER"
    )


    def getData():
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()
        print(mycursor.rowcount, "user inserted.")

    return getData()
