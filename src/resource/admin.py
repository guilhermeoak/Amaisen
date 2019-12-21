import sys
from src.resource.email_resource import Email
from src.service import sign_in
from src.service.add_customer import AddCustomer
from src.service.add_user import AddUser
from src.service.remove_user import RemoveUser
from src.service.select_users import SelectUser
from src.util.utils import clear_screen
from src.service.select_customers import SelectCustomer
from src.util.connection import insert_data


class Admin:

    def __init__(self):

        try:

            while True:

                print('\n1: Send emails')
                print('2: Add user')
                print('3: Add customer')
                print('4: Show users')
                print('5: Show customers')
                print('6: Delete user')
                print('7: Log out')
                print('q: Exit')

                number = str(input('\nChoose one: '))

                if number == 'q':
                    insert_data('UPDATE USER SET LOGADO = 0')
                    clear_screen()
                    print('System finished!')
                    sys.exit()
                if number == '1':
                    Email()
                    print(input('\nPress Enter to continue...'))
                    clear_screen()
                if number == '2':
                    AddUser()
                    print(input('\nPress Enter to continue...'))
                    clear_screen()
                if number == '3':
                    AddCustomer()
                    print(input('\nPress Enter to continue...'))
                    clear_screen()
                if number == '4':
                    SelectUser()
                    clear_screen()
                if number == '5':
                    SelectCustomer()
                    clear_screen()
                if number == '6':
                    RemoveUser()
                    clear_screen()
                if number == '7':
                    insert_data('UPDATE USER SET LOGADO = 0')
                    clear_screen()
                    break

        except KeyboardInterrupt:
            insert_data('UPDATE USER SET LOGADO = 0')
            clear_screen()
