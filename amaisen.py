#!/bin/bash

from src.resource.email_resource import Email
from src.service.add_user import AddUser
from src.service.sign_in import SignIn
from src.util.utils import whatToSay
from src.service.remove_user import RemoveUser
from src.service.select_users import SelectUser
from _datetime import datetime
import getpass
import subprocess

subprocess.run(['clear'])

user = getpass.getuser()
now = datetime.now()
print('\033[32m' + 'System started...\n' + whatToSay(now.hour), user.capitalize() + '\n' + '\033[0;0m')


def start():
    print('\nWhat do you want to do?')

    while True:

        print('\033[33m' + '1: New user registration' + '\033[0;0m')
        print('\033[33m' + '2: Login' + '\033[0;0m')

        number = str(input('\033[34m' + '\nChoose one: ' + '\033[0;0m'))

        if number == '1':
            AddUser()
        if number == '2':
            break

    print('\033[32m' + 'Put your login data in the respective fields' + '\033[0;0m' + '\n')

    sign_in = SignIn()
    my_email = sign_in.get_email(sign_in)

    while True:

        print('\n' + '\033[33m' + '1: Send emails' + '\033[0;0m')
        print('\033[33m' + '2: Add user' + '\033[0;0m')
        print('\033[33m' + '3: Show users' + '\033[0;0m')
        print('\033[33m' + '4: Delete user' + '\033[0;0m')
        print('\033[33m' + 'q: Exit' + '\033[0;0m')

        number = str(input('\033[32m' + '\nChoose one: ' + '\033[0;0m'))

        if number == '1':
            Email()
            print(input('Press Enter to continue...'))
        if number == '2':
            AddUser()
            print(input('Press Enter to continue...'))
        if number == '3':
            SelectUser()
            print(input('Press Enter to continue...'))
        if number == '4':
            RemoveUser()
        if number == 'q':
            print('\nBye!')
            break


start()
