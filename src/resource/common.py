import sys
from src.resource.email_resource import Email
from src.service.add_customer import AddCustomer
from src.util.utils import clear_screen
from src.service.select_customers import SelectCustomer


class Common:

    def __init__(self):

        while True:

            print('\n1: Send emails')
            print('2: Add customer')
            print('3: Show customers')
            print('4: Log out')
            print('q: Exit')

            number = str(input('\nChoose one: '))

            if number == 'q':
                clear_screen()
                print('System finished!')
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
