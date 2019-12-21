from src.util.utils import clear_screen
from src.util import connection as con


class SelectCustomer:

    def __init__(self):
        global code
        code = 1

        try:

            while code == 1:

                clear_screen()
                sql = 'SELECT * FROM CUSTOMER'
                result = con.select_data(sql)

                for customer in result:
                    print(customer)
                print(input('Press any key to continue...'))
                clear_screen()
                code = 0

        except KeyboardInterrupt:
            code = 0
