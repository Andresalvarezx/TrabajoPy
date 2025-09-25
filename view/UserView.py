from domain.User import User
from repository.UserRepository import UserRepository
from service.UserService import UserService


class UserView:

    def __init__(self):
        self.userRepository = UserRepository()
        self.userService = UserService()
        self.user = None

    def run_app(self):
        print("=== Menú de Usuarios ===")
        print("1. Registrar nuevo usuario")
        print("2. Listar usuarios")
        print("3. Salir")

    def menu_user(self):
        self.run_app()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            self.register_user()
        elif opcion == "2":
            self.list_users()
        else:
            print("Saliendo del menú de usuarios.")

    def register_user(self):
        id = input("ID del usuario: ")
        name = input("Nombre: ")
        phone = input("Teléfono: ")
        mail = input("Correo electrónico: ")

        user = User(id, name, phone, mail)
        self.userService.save_user(user)
        print("Usuario registrado con éxito.")

    def list_users(self):
        users = self.userService.get_all_users()
        for user in users:
            print(f"ID: {user.id}, Nombre: {user.name}, Teléfono: {user.phone}, Email: {user.mail}")
