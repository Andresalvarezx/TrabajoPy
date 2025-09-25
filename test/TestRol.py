
from service.RolService import RolService

if __name__ == "__main__":
    srv = RolService()
    srv.crear(1, "Administrador")
    print([ (r.id_rol, r.description) for r in srv.listar() ])
    print(srv.obtener(1))
    print(srv.actualizar(1, "Admin"))
    print(srv.eliminar(1))
