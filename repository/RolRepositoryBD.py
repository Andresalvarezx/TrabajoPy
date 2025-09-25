class Rol:
    
    def __init__(self, id_rol, description):
        self._id_rol = id_rol
        self._description = description

    @property
    def id_rol(self):
        return self._id_rol

    @id_rol.setter
    def id_rol(self, id_rol):
        self._id_rol = id_rol

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @staticmethod
    def from_row(row):
        """
        row debe ser una tupla proveniente de la BD en el orden:
        (id_rol, description)
        """
        return Rol(
            id_rol=row[0],
            description=row[1]
        )
