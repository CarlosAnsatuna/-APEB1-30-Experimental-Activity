# configuracion.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///universidad.db"
engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()