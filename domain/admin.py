from domain.User import User

class admin(User):

    # Constructor de la clase
    def __init__(self, id, name, phone, mail, department, level):
        super().__init__(id, name, phone, mail)
        self._department = department
        self._level = level

    @staticmethod
    def from_row(row):
        return admin(row[0], row[1], row[2], row[3], row[4], row[5])

    def __str__(self):
        return (f"Admin(id={self.id}, nombre={self.name}, telefono={self.phone}, "
                f"correo={self.mail}, departamento={self.department}, nivel={self.level})")

    def __repr__(self):
        return self.__str__()

    # Getters and Setters
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    # Métodos propios
    def grant_permission(self, permission):
        return f"Admin {self.name} ha otorgado el permiso: {permission}"

    def revoke_permission(self, permission):
        return f"Admin {self.name} ha revocado el permiso: {permission}"
