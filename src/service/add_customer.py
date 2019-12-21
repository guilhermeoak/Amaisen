from src.util import utils
from src.service.sign_in import SignIn
from src.util import connection as con


class AddCustomer:
    def __init__(self):
        global code
        code = 1

        try:

            while code == 1:

                utils.clear_screen()
                if utils.os_name != 'Windows':
                    utils.format_message('New Customer Registration')
                else:
                    print('New Customer Registration')

                if SignIn.get_user_type() == 'admin':

                    name = str(input('Name: '))
                    last_name = str(input('Last name: '))
                    email = str(input('Email: '))
                    interests = str(input('Interests: '))

                    query = ("INSERT INTO CUSTOMER (NAME, LASTNAME, EMAIL, TAG) VALUES('%s', '%s', '%s', '%s')" % (
                        name, last_name, email, interests))

                    con.insert_data(query)
                    code = 0

                else:
                    utils.clear_screen()
                    code = 0
                    print('You have no permissions to do it!')

        except KeyboardInterrupt:
            code = 0
