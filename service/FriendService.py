from domain.Friend import Friend
from repository.FriendRepository import FriendRepository
from repository.FriendRepositoryBD import FriendRepositoryDB


class  FriendService:


    def __init__(self):
        self.friendObject = Friend(None, None, None, None, None, None)
        self.friendRepository = FriendRepository()
        self.friendRepositoryDB = FriendRepositoryDB()



    def createUser(self):



        friend = []

        id = int(input("Id Amigo: "))
        self.friendObject.id = id
        name = input("Nombre amigo:")
        self.friendObject._name = name
        phone = input("Telefono: ")
        self.friendObject._phone= phone
        mail = input("Email: ")
        self.friendObject._mail = mail
        adress = (input("Direccion: "))
        self.friendObject._adress = adress
        rol = int(input("rol: "))
        self.friendObject._rol= rol

        friend.append(id) #1
        friend.append(name) #pepito
        friend.append(phone) # 3214567890
        friend.append(mail) # pp@mail.com
        friend.append(adress) #medellin
        friend.append(rol) # amigo

        print(f"friend{friend}")

        self.friendRepository.createFriendDict(id, friend)
        self.friendRepositoryDB.createFriendDB(self.friendObject)


    def selectUser(self):
        self.friendRepository.printFriend()
        return self.friendRepositoryDB.select_friends()


    def updateFriend(self , id_friend):
        friend = []


        if self.friendRepository.friends.get(id_friend):

            id = int(input("Id Amigo: "))
            self.friendObject.id = id
            name = input("Nombre amigo:")
            self.friendObject._name = name
            phone = input("Telefono: ")
            self.friendObject._phone = phone
            mail = input("Email: ")
            self.friendObject._mail = phone
            adress = (input("Direccion: "))
            self.friendObject._adress = adress
            rol = input("rol: ")
            self.friendObject._rol = adress

            friend.append(id)  # 1
            friend.append(name)  # pepito
            friend.append(phone)  # 3214567890
            friend.append(mail)  # pp@mail.com
            friend.append(adress)  # medellin
            friend.append(rol)  # amigo

            print(f"friend{friend}")

            self.friendRepository.createFriendDict(id, friend)
        else:
            print("Usuario no existe")



    def select_friend_by_id(self, id_friend):
        return self.friendRepositoryDB.select_user_by_id(id_friend)


    def update_friend(self):


        id = int(input("Ingrese el Id Amigo a modificar: "))
        self.friendObject.id = id


        name = input("Nombre amigo:")
        self.friendObject._name = name
        phone = input("Telefono: ")
        self.friendObject._phone = phone
        mail = input("Email: ")
        self.friendObject._mail = phone
        adress = (input("Direccion: "))
        self.friendObject._adress = adress
        rol = input("rol: ")
        self.friendObject._rol = adress

        self.friendRepositoryDB.updateFriend(self.friendObject)


    def removeFriend(self, id_friend):
        """self.friendRepository.removeFriendDict(id_friend)"""
        self.friendRepositoryDB.delete_friend_by_id(id_friend)