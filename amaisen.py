#!/bin/bash

from src.resource.email_resource import Email
from src.service.add_user import AddUser
from src.service.sign_in import SignIn
from src.util.utils import format_message
from src.util.utils import welcome
from src.service.remove_user import RemoveUser
from src.service.select_users import SelectUser
import subprocess
import sys
from datetime import datetime

subprocess.run(['clear'])

now = datetime.now()
message = ('\033[34m' + welcome(now.hour) + ' Amaisen is running' + '\033[0;0m')
format_message(message)


def start():
    while True:

        print('\033[33m' + '1: New user registration' + '\033[0;0m')
        print('\033[33m' + '2: Login' + '\033[0;0m')
        print('\033[33m' + 'q: Exit' + '\033[0;0m')

        number = str(input('\033[34m' + '\nChoose one: ' + '\033[0;0m'))

        if number == 'q':
            subprocess.run(['clear'])
            print('\033[31m' + 'System finished!' + '\033[0;0m')
            sys.exit()
        if number == '1':
            AddUser()
        if number == '2':
            break

    sign_in = SignIn()
    sign_in.sign_in()

    while True:

        print('\n' + '\033[33m' + '1: Send emails' + '\033[0;0m')
        print('\033[33m' + '2: Add user' + '\033[0;0m')
        print('\033[33m' + '3: Show users' + '\033[0;0m')
        print('\033[33m' + '4: Delete user' + '\033[0;0m')
        print('\033[33m' + '5: Log out' + '\033[0;0m')
        print('\033[33m' + 'q: Exit' + '\033[0;0m')

        number = str(input('\033[32m' + '\nChoose one: ' + '\033[0;0m'))

        if number == 'q':
            subprocess.run(['clear'])
            print('\033[31m' + 'System finished!' + '\033[0;0m')
            sys.exit()
        if number == '1':
            Email()
            print(input('Press Enter to continue...'))
            subprocess.run(['clear'])
        if number == '2':
            AddUser()
            print(input('Press Enter to continue...'))
            subprocess.run(['clear'])
        if number == '3':
            SelectUser()
            print(input('Press Enter to continue...'))
            subprocess.run(['clear'])
        if number == '4':
            RemoveUser()
            subprocess.run(['clear'])
        if number == '5':
            subprocess.run(['clear'])
            start()


start()
