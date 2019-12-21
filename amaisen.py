from src.service.sign_in import SignIn
from src.resource.admin import Admin
from src.resource.common import Common
from src.service.init import Init
from src.util.utils import clear_screen
import sys

while True:

    try:

        Init()

        SignIn.sign_in()

        if SignIn.get_user_type() == 'admin':
            Admin()
        else:
            Common()

    except KeyboardInterrupt:
        clear_screen()
        print('System finished!')
        sys.exit()
