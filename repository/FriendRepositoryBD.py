
from repository.Conexion import conexion

class FriendRepositoryDB:


    def __init__(self,):
        self.db = conexion(host='localhost', port=3306, user='root', password="", database='book_app')
        self.db.connect()



    def crearteFriendDB(self, friend):
        query = "INSERT INTO friend (id, name, phone, mail, adress , rol) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (
            friend.id,
            friend.name,
            friend.phone,
            friend.mail,
            friend.adress,
            friend.rol
        )
        self.db.execute_query(query, values)