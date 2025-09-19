from repository.Conexion import conexion
from domain.admin import admin

class AdminRepositoryDB:

    def __init__(self):
        self.db = conexion(host='localhost', port=3306, user='root', password="", database='book_app')
        self.db.connect()

    def createAdminDB(self, admin):
        query = "INSERT INTO admin (id, name, phone, mail, adress, rol) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (
            admin.id,
            admin.name,
            admin.phone,
            admin.mail,
            admin.adress,
            admin.rol
        )
        self.db.execute_query(query, values)

    def select_admins(self):
        query = "SELECT * FROM admin"
        result = self.db.execute_query(query)
        if result:
            admin_list = []
            for row in result:
                admin = admin.from_row(row)
                admin_list.append(admin)
            return admin_list
        else:
            print("Registros no encontrados")
            return []

    def select_admin_by_id(self, id_admin):
        query = "SELECT * FROM admin WHERE id=%s"
        result = self.db.execute_query(query, (id_admin,))
        if result:
            return admin.from_row(result[0])
        else:
            print("Registro no encontrado")
            return []

    def updateAdmin(self, admin):
        query = "UPDATE admin SET name=%s, phone=%s, mail=%s, adress=%s, rol=%s WHERE id=%s"
        values = (admin.name, admin.phone, admin.mail, admin.adress, admin.rol, admin.id)
        self.db.execute_query(query, values)

    def delete_admin_by_id(self, id):
        query = "DELETE FROM admin WHERE id=%s"
        self.db.execute_query(query, [id])
