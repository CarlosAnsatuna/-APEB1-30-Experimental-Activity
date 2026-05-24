# consulta_or.py
from configuracion import session
from crear_base_entidades import AcademicResources
from sqlalchemy import or_

print("--- TIPO DE CONSULTA: LOGICAL OR ---")

# Buscamos recursos que cumplan cualquiera de las dos condiciones
recursos_or = session.query(AcademicResources).filter(
    or_(
        AcademicResources.type_resource == "Video",
        AcademicResources.title.like("%Framework%")
    )
).all()

for r in recursos_or:
    print(f"Recurso Encontrado: {r.title} | Tipo: {r.type_resource}")