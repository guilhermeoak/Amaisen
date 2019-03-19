from src.util.utils import clear_screen
from src.util import connection as con


class SelectCustomer:

    def __init__(self):
        clear_screen()
        sql = 'SELECT * FROM CUSTOMER'
        result = con.select_data(sql)

        for customer in result:
            print(customer)
        print(input('Press any key to continue...'))
        clear_screen()
