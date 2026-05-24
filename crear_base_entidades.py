# crear_base_entidades.py
# El documento se hizo con nombres en ingles por fines de llevar registro para un portafolio de git-hub
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from configuracion import Base, engine

class Faculty(Base):
    __tablename__ = 'faculty'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    name_dean = Column(String, nullable=False)
    
    # Cross-relationships (One to many)
    carrers = relationship("Carrers", back_populates="faculty")


class Carrers(Base):
    __tablename__ = 'carrers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    intern_code = Column(String, unique=True, nullable=False)
    faculty_id = Column(Integer, ForeignKey('faculty.id'), nullable=False)
    
    # Cross-relationships (Foreign Keys)
    faculty = relationship("Faculty", back_populates="carrers")
    teachers = relationship("Teachers", back_populates="carrer")


class Teachers(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    area_speciality = Column(String, nullable=False)
    carrers_id = Column(Integer, ForeignKey('carrers.id'), nullable=False)
    
    carrer = relationship("Carrers", back_populates="teachers")
    academic_resources = relationship("AcademicResources", back_populates="teacher")


class AcademicResources(Base):
    __tablename__ = 'academic_resources'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    type_resource = Column(String, nullable=False)
    URL = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    
    teacher = relationship("Teachers", back_populates="academic_resources")


if __name__ == "__main__":
    print("Conectando con el motor y creando tablas...")
    Base.metadata.create_all(engine)
    print("¡Base de datos 'universidad.db' generada y tablas creadas exitosamente!")