from domain.Friend import Friend
from repository.FriendRespository import FriendRepositoryDB
from service.FriendService import FriendService
from repository.FriendRepositoryBD import FriendRepository


class App:


    def __init__(self):
        self.friendRepository = FriendRepository()
        self.friendRepositoryDB = FriendRepositoryDB()
        self.friendService = FriendService()
        self.friend = Friend()

    def run_app(self):
        print("Presione 1 para iniciar ")
        init = int(input("Ingrese 1 para inicializar la aplicacion: "))
        while init != 0:
            option = int(input("Ingrese 1. Gestionar amigos \n 2. Gestionar Mis Objectos \n "
                               "3. Gestionar Mis Prestamos \n"
                               "4. Salir "))
            match option:
                case 1:
                    print("Gestion de Amigos")
                    self.menu_friend()
                case 2:
                    print("Gestion de Mis Prestamos")
                case 3:
                    print("Gestion de Mis Amigos")
                case 4:
                    print("Salir")
                case _:
                    print("Seleccione una opcion valida")



    def menu_friend(self):
        print("Menú Amigo")