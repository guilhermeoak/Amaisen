from . import connection as con

tableList = []


def set_table():
    global varTable

    i = 0
    sql = 'SHOW TABLES;'

    print('\n' + '\033[33m' + 'Who will you sent emails for? ' + '\033[0;0m' + '\n')

    result = con.setData(sql)

    for table in result:
        tableList.append(table)
        print('[%i]' % i, table)
        i += 1

    tb = int(input('\n' + '\033[33m' + 'Option: ' + '\033[0;0m'))

    varTable = tableList[tb]

    return varTable
