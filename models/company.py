from sqlalchemy import create_engine, Integer, Numeric, String, Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base, declared_attr


Base = declarative_base()

def connect_db():
    conn_str = 'mysql+mysqldb://root:root@localhost/orm'
    return create_engine(conn_str)

class Departamentos(Base):
    __tablename__="departamento"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))

class Funcionarios(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(150))
    id_departamento = Column(Integer, ForeignKey("departamento.id"))
    departamento = relationship(Departamentos, backref=backref("funcionarios", uselist=True))