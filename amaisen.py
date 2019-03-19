#!/bin/bash
from src.service.sign_in import SignIn
from src.resource.admin import Admin
from src.resource.common import Common
from src.service.init import Init

while True:

    Init()

    sign_in = SignIn()
    sign_in.sign_in()

    if sign_in.get_user_type() == 'admin':
        Admin.exec_admin()
    else:
        Common.exec_common()
