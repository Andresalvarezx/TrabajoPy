from domain.admin import admin
from repository.adminRepository import adminRespository
from repository.FriendRepositoryBD import adminRepositoryBD

class adminService:

    def __init__(self):
        self.adminObject = admin(None, None, None, None, None, None)
        self.adminRepository = adminRespository()
        self.adminRepositoryDB = adminRepositoryBD()

    def createAdmin(self):
        admin = []

        id = int(input("Id Admin: "))
        self.adminObject.id = id
        name = input("Nombre Admin: ")
        self.adminObject._name = name
        phone = input("Teléfono: ")
        self.adminObject._phone = phone
        mail = input("Email: ")
        self.adminObject._mail = mail
        address = input("Dirección: ")
        self.adminObject._address = address
        rol = int(input("Rol: "))
        self.adminObject._rol = rol

        admin.extend([id, name, phone, mail, address, rol])
        print(f"admin: {admin}")

        self.adminRepository.createAdminDict(id, admin)
        self.adminRepositoryDB.createAdminDB(self.adminObject)

    def selectAdmin(self):
        self.adminRepository.printAdmin()
        return self.adminRepositoryDB.select_admins()

    def updateAdmin(self, id_admin):
        admin = []

        if self.adminRepository.admins.get(id_admin):
            id = int(input("Nuevo Id Admin: "))
            self.adminObject.id = id
            name = input("Nuevo nombre: ")
            self.adminObject._name = name
            phone = input("Nuevo teléfono: ")
            self.adminObject._phone = phone
            mail = input("Nuevo email: ")
            self.adminObject._mail = mail
            address = input("Nueva dirección: ")
            self.adminObject._address = address
            rol = int(input("Nuevo rol: "))
            self.adminObject._rol = rol

            admin.extend([id, name, phone, mail, address, rol])
            print(f"admin actualizado: {admin}")

            self.adminRepository.createAdminDict(id, admin)
        else:
            print("Admin no existe")

    def select_admin_by_id(self, id_admin):
        return self.adminRepositoryDB.select_admin_by_id(id_admin)

    def update_admin(self):
        id = int(input("Ingrese el Id Admin a modificar: "))
        self.adminObject.id = id

        name = input("Nuevo nombre: ")
        self.adminObject._name = name
        phone = input("Nuevo teléfono: ")
        self.adminObject._phone = phone
        mail = input("Nuevo email: ")
        self.adminObject._mail = mail
        address = input("Nueva dirección: ")
        self.adminObject._address = address
        rol = int(input("Nuevo rol: "))
        self.adminObject._rol = rol

        self.adminRepositoryDB.updateAdmin(self.adminObject)

    def removeAdmin(self, id_admin):
        """self.adminRepository.removeAdminDict(id_admin)"""
        self.adminRepositoryDB.delete_admin_by_id(id_admin)
