#!/bin/bash

from src.service import add_user
import src.resource.email_resource as EmailResource
import subprocess

print('\nWhato do you want to do?')


def start():
    subprocess.run(['clear'])
    print('\033[33m' + '1: Send emails' + '\033[0;0m')
    print('\033[33m' + '2: New user registration' + '\033[0;0m')
    print('\033[33m' + 'q: Exit' + '\033[0;0m')

    number = str(input('\033[32m' + '\nChoose one: ' + '\033[0;0m'))

    def options(option):
        if option == '1':
            return EmailResource.send_email()
        if option == '2':
            return add_user.register_user()
        if option == 'q':
            return False

    return options(number)


while True:
    start()
