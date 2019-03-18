from . import connection as con
from .utils import format_message
from src.util.utils import clear_screen

tableList = []


def set_table():
    clear_screen()
    global varTable

    i = 0
    sql = 'SHOW TABLES;'

    format_message('\033[33m' + 'Who will you sent emails for? ' + '\033[0;0m')

    result = con.select_data(sql)

    for table in result:
        tableList.append(table)
        print('[%i]' % i, table)
        i += 1

    tb = int(input('\n' + '\033[33m' + 'Option: ' + '\033[0;0m'))

    varTable = tableList[tb]

    return varTable
