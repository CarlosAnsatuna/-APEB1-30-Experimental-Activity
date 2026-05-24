# poblar_base.py
from datetime import date
from configuracion import session
from crear_base_entidades import Faculty, Carrers, Teachers, AcademicResources

def poblar():
    print("Iniciando la inserción de registros de prueba...")

    # 1. Creamos Facultades
    f1 = Faculty(name="Faculty of Engineering", location="Building A - Main Campus", name_dean="Dr. Alan Turing")
    f2 = Faculty(name="Faculty of Science", location="Building B - West Wing", name_dean="Dra. Marie Curie")
    session.add_all([f1, f2])
    session.commit()  # Guardamos para generar sus IDs fijos

    # 2. Creamos Carreras vinculadas a las facultades
    c1 = Carrers(name="Cybersecurity and Risk Management", intern_code="CYBER-101", faculty_id=f1.id)
    c2 = Carrers(name="Software Development", intern_code="SOFT-202", faculty_id=f1.id)
    c3 = Carrers(name="Data Science", intern_code="DATA-303", faculty_id=f2.id)
    session.add_all([c1, c2, c3])
    session.commit()

    # 3. Creamos Profesores asignados a sus respectivas carreras
    t1 = Teachers(name="Jean-Pierre", last_name="Polnareff", email="jpolnareff@uni.edu", area_speciality="Network Security", carrers_id=c1.id)
    t2 = Teachers(name="Arthur", last_name="Pendragon", email="apendragon@uni.edu", area_speciality="GRC and IT Auditing", carrers_id=c1.id)
    t3 = Teachers(name="Linus", last_name="Torvalds", email="ltorvalds@uni.edu", area_speciality="Operating Systems", carrers_id=c2.id)
    session.add_all([t1, t2, t3])
    session.commit()

    # 4. Creamos Recursos Académicos enlazados a los profesores creadores
    r1 = AcademicResources(
        title="CIS Controls v8 Compliance Framework", 
        date=date(2025, 4, 12), 
        type_resource="Guide", 
        URL="https://uni.edu/resources/cis-framework-v8", 
        teacher_id=t2.id
    )
    r2 = AcademicResources(
        title="SOC Analysis Basics with Kibana and Elasticsearch", 
        date=date(2026, 2, 18), 
        type_resource="Video", 
        URL="https://uni.edu/resources/soc-kibana-intro", 
        teacher_id=t1.id
    )
    r3 = AcademicResources(
        title="Linux Kernel Architecture from Scratch", 
        date=date(2026, 5, 10), 
        type_resource="Book", 
        URL="https://uni.edu/resources/linux-kernel-book", 
        teacher_id=t3.id
    )
    session.add_all([r1, r2, r3])
    session.commit()

    print("¡Base de datos poblada exitosamente con registros iniciales!")

if __name__ == "__main__":
    poblar()