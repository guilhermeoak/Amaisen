class Customer:

    def __init__(self, name, last_name, email, interests):
        self.name = name,
        self.last_name = last_name,
        self.email = email,
        self.interests = interests

    # ------------setters--------------------------------------

    def set_name(self, name):
        self.name = name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email):
        self.email = email

    def set_interests(self, interests):
        self.interests = interests

    # ------------getters--------------------------------------

    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_interests(self):
        return self.interests
