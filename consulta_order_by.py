# consulta_order_by.py
from configuracion import session
from crear_base_entidades import AcademicResources

print("--- TIPO DE CONSULTA: ORDER_BY ---")
print("Recursos Académicos (Ordenados del más reciente al más antiguo):")

# Usamos .desc() para orden descendente
recursos_ordenados = session.query(AcademicResources).order_by(AcademicResources.date.desc()).all()

for r in recursos_ordenados:
    print(f"Fecha: {r.date} | Título: {r.title} | Tipo: {r.type_resource}")