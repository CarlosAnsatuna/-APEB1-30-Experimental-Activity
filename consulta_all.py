from configuracion import session
from crear_base_entidades import Faculty

print("--- TIPO DE CONSULTA: ALL ---")
print("Listado completo de Facultades:")

# Traemos todos los registros de la tabla Faculty
facultades = session.query(Faculty).all()

for f in facultades:
    print(f"ID: {f.id} | Facultad: {f.name} | Decano: {f.name_dean} | Ubicación: {f.location}")