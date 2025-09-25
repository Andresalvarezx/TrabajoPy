from domain.Rol import Rol
from repository.RolRepository import RolRepository
from repository.RolRepositoryDB import RolRepositoryDB
from service.RolService import RolService


class AppRol:

    def __init__(self):
        self.rolRepository = RolRepository()
        self.rolRepositoryDB = RolRepositoryDB()
        self.rolService = RolService()
        self.rol = Rol(None, None)

    def run_app(self):
        print("Presione 1 para iniciar ")
        init = int(input("Ingrese 1 para inicializar la aplicación: "))
        while init != 0:
            option = int(input(
                "Ingrese una opción:\n"
                "1. Gestionar Roles\n"
                "2. Salir\n"
            ))
            match option:
                case 1:
                    print("Gestión de Roles")
                    self.menu_rol()
                case 2:
                    print("Salir")
                    init = 0
                case _:
                    print("Seleccione una opción válida")

    def menu_rol(self):
        while True:
            print(
                "\nMenú Rol\n"
                "1. Crear rol\n"
                "2. Listar roles (DB)\n"
                "3. Buscar rol por id (DB)\n"
                "4. Actualizar rol (DB)\n"
                "5. Eliminar rol (DB)\n"
                "6. Mostrar roles en memoria\n"
                "7. Volver\n"
            )
            option = int(input("Opción: "))

            match option:
                case 1:
                   
                    self.rolService.createRol()
                case 2:
                    roles = self.rolService.selectRoles()
                    print(f"roles {roles}")
                case 3:
                    id_rol = int(input("Id Rol a consultar: "))
                    rol = self.rolService.select_rol_by_id(id_rol)
                    print(f"rol {rol}")
                case 4:
                    
                    self.rolService.update_rol()
                case 5:
                    id_rol = int(input("Id Rol a eliminar: "))
                    self.rolService.removeRol(id_rol)
                    print("Rol eliminado si existía.")
                case 6:
                    
                    self.rolRepository.printRol()
                case 7:
                    break
                case _:
                    print("Seleccione una opción válida")


if __name__ == "__main__":
    AppRol().run_app()
