class AdminRepository:

    def __init__(self):
        self.admins = {}

    def createAdminDict(self, id_admin, admin):
        self.admins.update({id_admin: admin})

    def printAdmin(self):
        print(self.admins)

    def updateAdminDict(self, id_admin, admin):
        self.admins.update({id_admin: admin})

    def removeAdminDict(self, id_admin):
        self.admins.pop(id_admin, None)
