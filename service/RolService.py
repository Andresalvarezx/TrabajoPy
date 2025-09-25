from domain.Rol import Rol
from repository.RolRepository import RolRepository
from repository.RolRepositoryBD import RolRepositoryDB


class RolService:

    def __init__(self):
        self.rolObject = Rol(None, None)
        self.rolRepository = RolRepository()
        self.rolRepositoryDB = RolRepositoryDB()

    
    def createRol(self):
        rol_list = []

        id_rol = int(input("Id Rol: "))
        self.rolObject.id_rol = id_rol
        description = input("Descripción del rol: ")
        self.rolObject._description = description

        rol_list.append(id_rol)
        rol_list.append(description)

        print(f"rol{rol_list}")

        self.rolRepository.createRolDict(id_rol, rol_list)
        self.rolRepositoryDB.createRolDB(self.rolObject)

   
    def selectRoles(self):
        self.rolRepository.printRol()
        return self.rolRepositoryDB.select_roles()

    
    def updateRolInMemory(self, id_rol):
        if self.rolRepository.roles.get(id_rol):
            rol_list = []

            id_new = int(input("Nuevo Id Rol: "))
            self.rolObject.id_rol = id_new
            description = input("Nueva descripción del rol: ")
            self.rolObject._description = description

            rol_list.append(id_new)
            rol_list.append(description)

            print(f"rol{rol_list}")

            self.rolRepository.updateRolDict(id_new, rol_list)
        else:
            print("Rol no existe en memoria")

    
    def select_rol_by_id(self, id_rol):
        return self.rolRepositoryDB.select_rol_by_id(id_rol)

    
    def update_rol(self):
        id_rol = int(input("Ingrese el Id Rol a modificar: "))
        self.rolObject.id_rol = id_rol

        description = input("Nueva descripción del rol: ")
        self.rolObject._description = description

        self.rolRepositoryDB.updateRol(self.rolObject)

    
    def removeRol(self, id_rol):
        """self.rolRepository.removeRolDict(id_rol)"""
        self.rolRepositoryDB.delete_rol_by_id(id_rol)
