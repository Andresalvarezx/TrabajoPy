
from domain.admin import admin
from service.adminSerivice import adminService



# Crear una instancia vacía de admin
admin_obj = admin(id=None, name=None, phone=None, mail=None, department=None, level=None)

# Crear instancia del servicio
adminService = adminService()

# Buscar un admin por ID
show_admin = adminService.select_admin_by_id(12345678)  # Cambia este ID por uno que exista en tu base de datos
print("Admin:", show_admin)
