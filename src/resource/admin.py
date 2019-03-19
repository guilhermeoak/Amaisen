import sys
from src.resource.email_resource import Email
from src.service import sign_in
from src.service.add_customer import AddCustomer
from src.service.add_user import AddUser
from src.service.remove_user import RemoveUser
from src.service.select_users import SelectUser
from src.util.utils import clear_screen


class Admin:

    def __init__(self):

        while True:

            print('\n' + '\033[33m' + '1: Send emails' + '\033[0;0m')
            print('\033[33m' + '2: Add user' + '\033[0;0m')
            print('\033[33m' + '3: Add customer' + '\033[0;0m')
            print('\033[33m' + '4: Show users' + '\033[0;0m')
            print('\033[33m' + '5: Delete user' + '\033[0;0m')
            print('\033[33m' + '6: Log out' + '\033[0;0m')
            print('\033[33m' + 'q: Exit' + '\033[0;0m')

            number = str(input('\033[32m' + '\nChoose one: ' + '\033[0;0m'))

            if number == 'q':
                clear_screen()
                print('\033[31m' + 'System finished!' + '\033[0;0m')
                sys.exit()
            if number == '1':
                Email()
                print(input('Press Enter to continue...'))
                clear_screen()
            if number == '2':
                AddUser()
                print(input('Press Enter to continue...'))
                clear_screen()
            if number == '3':
                AddCustomer()
                print(input('Press Enter to continue...'))
                clear_screen()
            if number == '4':
                SelectUser()
                clear_screen()
            if number == '5':
                RemoveUser()
                clear_screen()
            if number == '6':
                clear_screen()
                break
