class RolRepository:
    
    def __init__(self):
        self.roles = {}

    def createRolDict(self, id_rol, rol):
        self.roles.update({id_rol: rol})

    def printRol(self):
        print(self.roles)

    def updateRolDict(self, id_rol, rol):
        self.roles.update({id_rol: rol})

    def removeRolDict(self, id_rol):
        self.roles.pop(id_rol)
