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