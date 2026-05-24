# consulta_and.py
from configuracion import session
from crear_base_entidades import Teachers
from sqlalchemy import and_

print("--- TIPO DE CONSULTA: LOGICAL AND ---")

# Ambas condiciones deben cumplirse obligatoriamente
profesores_and = session.query(Teachers).filter(
    and_(
        Teachers.last_name == "Pendragon",
        Teachers.carrers_id == 1
    )
).all()

for t in profesores_and:
    print(f"Profesor validado: {t.name} {t.last_name} | Especialidad: {t.area_speciality}")