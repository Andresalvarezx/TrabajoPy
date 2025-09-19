from domain.admin import admin
from repository.adminRepository import adminRepository
from repository.adminRepositoryBD import adminRepositoryBD
from service.adminSerivice import adminService



class AppAdmin:

    def __init__(self):
        self.adminRepository = adminRepository()
        self.adminRepositoryDB = adminRepositoryBD()
        self.adminService = adminService()
        self.admin = admin(None, None, None, None, None, None)

    def run_app_admin(self):
        print("Presione 1 para iniciar ")
        init = int(input("Ingrese 1 para inicializar la gestión de admins: "))
        while init != 0:
            option = int(input("Ingrese una opción:\n"
                               "1. Crear Admin\n"
                               "2. Ver todos los Admins\n"
                               "3. Buscar Admin por ID\n"
                               "4. Actualizar Admin\n"
                               "5. Eliminar Admin\n"
                               "6. Salir\n"))
            match option:
                case 1:
                    self.adminService.createAdmin()
                case 2:
                    admins = self.adminService.selectAdmin()
                    for adm in admins:
                        print(adm)
                case 3:
                    id_admin = int(input("Ingrese el ID del admin: "))
                    admin_found = self.adminService.select_admin_by_id(id_admin)
                    print(admin_found)
                case 4:
                    self.adminService.update_admin()
                case 5:
                    id_admin = int(input("Ingrese el ID del admin a eliminar: "))
                    self.adminService.removeAdmin(id_admin)
                case 6:
                    print("Saliendo de la gestión de admins.")
                    break
                case _:
                    print("Seleccione una opción válida.")
