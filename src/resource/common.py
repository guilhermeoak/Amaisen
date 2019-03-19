import sys
from src.resource.email_resource import Email
from src.service.add_customer import AddCustomer
from src.util.utils import clear_screen
from src.service.select_customers import SelectCustomer


class Common:

    def __init__(self):

        while True:

            print('\n' + '\033[33m' + '1: Send emails' + '\033[0;0m')
            print('\033[33m' + '2: Add customer' + '\033[0;0m')
            print('\033[33m' + '3: Show customers' + '\033[0;0m')
            print('\033[33m' + '4: Log out' + '\033[0;0m')
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
                AddCustomer()
                print(input('Press Enter to continue...'))
                clear_screen()
            if number == '3':
                SelectCustomer()
                clear_screen()
            if number == '4':
                clear_screen()
                break
