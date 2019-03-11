from . import Connection as con
import getpass

__all__ = ['whatToSay', 'tableList', 'setTable', 'getTable', 'sign_in']


def sign_in():

    def __init__():
        global result
        login = str(input('Login: '))
        passwd = getpass.getpass(prompt='Password: ')
        query = ('SELECT LOGIN, PASSWORD FROM USER WHERE TYPE = "admin" and LOGIN = %s AND PASSWORD = %s;' % (
                login, passwd))
        result = con.setData(login, passwd, query)
    
        if len(result) > 0:
            return result
        else:
            print('Login or Password wrong, please try again!')
            sign_in()


def whatToSay(hour):
    if hour >= 00 and hour < 12:
        return 'Good morning'
    if hour >= 12 and hour < 18:
        return 'Good afternoon'
    if hour >= 18 and hour <= 23:
        return 'Good evening'


tableList = []


def setTable():
    i = 0
    sql = ('SHOW TABLES;')
    global varTable
    print('Which table you wish use? ')
    result = con.setData('guilherme', '3141', sql)
    for table in result:
        tableList.append(table)
        print('[%i]' % i, table)
        i += 1
    tb = int(input('table: '))
    varTable = tableList[tb]


def getTable():
    return varTable


sign_in()