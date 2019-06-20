from src.service.sign_in import SignIn
from src.resource.admin import Admin
from src.resource.common import Common
from src.service.init import Init

while True:

    Init()

    SignIn.sign_in()

    if SignIn.get_user_type() == 'admin':
        Admin()
    else:
        Common()
