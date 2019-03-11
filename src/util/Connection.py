import mysql.connector


def setData(user, passwd, query):
    mydb = mysql.connector.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        database="USER"
    )

    def getData():
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result

    return getData()
