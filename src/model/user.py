class User:
    
    def __init__(self, name, lastname, tp, email, login, password):
        self.name = name
        self.lastname = lastname
        self.tp = tp #type of account
        self.email = email
        self.login = login
        self.password = password

    
    def setName(self, name):
        self.name = name

    def setLastname(self, lastname):
        self.lastname = lastname
    
    def setTp(self, tp):
        self.tp = tp

    def setEmail(self, email):
        self.email = email

    def setLogin(self, login):
        self.login = login

    def setPassword(self, passowd):
        self.passowd = passowd

    def getName(self):
        return self.name

    def getLastname(self):
        return self.lastname

    def getTp(self):
        return self.tp

    def getEmail(self):
        return self.email

    def getLogin(self):
        return self.login

    def getPassword(self):
        return self.passowd


        
