
from domain.Rol import Rol
from repository.RolRepositoryBD import RolRepositoryBD


class RolService:
    def __init__(self):
        self.repo = RolRepositoryBD()

    def createRol(self):
        id_rol = int(input("Id Rol: "))
        description = input("Descripción del rol: ")

        # crear objeto Rol con los datos
        rol = Rol(id_rol, description)

        # guardar en BD
        self.repo.create(rol)

        print(f"Rol creado: {rol.id_rol} - {rol.description}")
