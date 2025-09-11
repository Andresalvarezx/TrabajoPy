from domain.User import User


class Friend (User):

    # Constructor de la clase

    def __init__(self, id, name, phone, mail, adress, rol):
        super().__init__(id, name, phone, mail)
        self._adress = adress
        self._rol = rol




    #Getters and Setters

    @property
    def adress(self):
        return self._adress

    @adress.setter
    def adress(self, adress):
        self._adress = adress

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol



    