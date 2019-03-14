class User:

    def __init__(self, name, last_name, tp, email, login, password):
        self.name = name
        self.last_name = last_name
        self.tp = tp  # type of account
        self.email = email
        self.login = login
        self.password = password

    # ------------setters--------------------------------------

    def set_name(self, name):
        self.name = name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_tp(self, tp):
        self.tp = tp

    def set_email(self, email):
        self.email = email

    def set_login(self, login):
        self.login = login

    def set_password(self, password):
        self.password = password

    # ------------getters--------------------------------------

    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_tp(self):
        return self.tp

    def get_email(self):
        return self.email

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password
