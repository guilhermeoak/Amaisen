import os
import platform
import getpass
import subprocess
from . import connection as con
import settings

os_name = platform.system()

def welcome(hour):
    if 00 <= hour < 12:
        return 'Good morning!'
    if 12 <= hour < 18:
        return 'Good afternoon!'
    if 18 <= hour <= 23:
        return 'Good evening!'



def format_message(message):
    y, x = os.popen('stty size', 'r').read().split()
    space = ''
    count = 0
    while count < (int(x) / 3):
        space = space + ' '
        count += 1

    print(space, message)


def clear_screen():    
    if os_name == 'Linux' or os_name == 'Mac':
        subprocess.run(['clear'])
    if os_name == 'Windows':
        os.system('cls')


def check_database(): 
    def get_data():
        my_cursor = con.mydb.cursor()
        my_cursor.execute('CREATE DATABASE IF NOT EXISTS USER;')        
        con.mydb.commit()

    return get_data()


def check_tables():
    tables = [
        'CREATE TABLE IF NOT EXISTS USER(ID INT AUTO_INCREMENT PRIMARY KEY, TYPE VARCHAR(255), LOGIN VARCHAR(255), '
        'PASSWORD VARCHAR(255), NAME VARCHAR(255), LASTNAME VARCHAR(255), EMAIL VARCHAR(255));',
        'CREATE TABLE IF NOT EXISTS CUSTOMER(ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(255), LASTNAME VARCHAR('
        '255), EMAIL VARCHAR(255), TAG VARCHAR(255));']

    def get_data():
        my_cursor = con.mydb.cursor()
        for table in tables:
            my_cursor.execute(table)
        con.mydb.commit()

    return get_data()


def check_user():
    query = 'SELECT TYPE FROM USER'

    def get_data():
        my_cursor = con.mydb.cursor()
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        if len(result) > 0:
            return True

    return get_data()
