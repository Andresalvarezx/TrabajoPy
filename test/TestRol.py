from domain.Rol import Rol
from service.RolService import RolService


rol = Rol(None, None)
rolService = RolService()

show_rol = rolService.select_rol_by_id(1)
print(f"rol {show_rol}")
