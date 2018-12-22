from sqlalchemy import create_engine, Integer, Numeric, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base, declared_attr


Base = declarative_base()

def connect_db():
    conn_str = 'mysql+mysqldb://root:root@localhost/orm'
    return create_engine(conn_str)


class Pessoa(Base):
    __tablename__="pessoa"
    id   = Column(Integer, primary_key=True)
    nome = Column(String(250), nullable=False)

class Endereco(Base):
    __tablename__ = "endereco"
    id = Column(Integer, primary_key=True)
    nome_rua = Column(String(250))
    numero = Column(String(250))
    #cep = Column(String(9))
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship(Pessoa)

if __name__ == "__main__":
    print(Pessoa.__mapper__)
    print(Pessoa.__table__)