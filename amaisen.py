#!/bin/bash
from src.service.sign_in import SignIn
from src.util.utils import format_message
from src.util.utils import welcome
from src.util.utils import clear_screen
from src.util import utils
from src.resource.admin import Admin
from src.resource.common import Common
from src.service.init import Init
from datetime import datetime

clear_screen()

now = datetime.now()
message = ('\033[34m' + welcome(now.hour) + ' Amaisen is running' + '\033[0;0m')
format_message(message)

utils.check_database()
utils.check_tables()


def start():
    while True:

        Init.init()

        sign_in = SignIn()
        sign_in.sign_in()

        if sign_in.get_user_type() == 'admin':
            Admin.exec_admin()
        else:
            Common.exec_common()


start()
