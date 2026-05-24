# consulta_filter.py
from configuracion import session
from crear_base_entidades import Teachers

print("--- TIPO DE CONSULTA: FILTER ---")
print("Profesores expertos en Sistemas Operativos:")

# Filtramos usando el operador ==
profesores_os = session.query(Teachers).filter(Teachers.area_speciality == "Operating Systems").all()

for t in profesores_os:
    print(f"Profesor: {t.name} {t.last_name} | Email: {t.email}")