from sqlalchemy import create_engine, Integer, Numeric, String, Column, ForeignKey
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr


def connect_db():
    conn_str = 'mysql+mysqldb://root:root@localhost/orm'
    return create_engine(conn_str)

engine = connect_db()
Base = declarative_base()


class Departamentos(Base):
    __tablename__="departamento"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    funcionarios = relationship('Funcionarios', secondary='func_depart')

class Funcionarios(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(150))
    departamentos = relationship('Departamentos', secondary="func_depart")
    cargo = relationship('Cargo', secondary="func_depart")
    
class Cargo(Base):
    __tablename__ = 'cargo'
    id = Column(Integer, primary_key=True)
    nome = Column(String(150))
    funcionarios = relationship('Funcionarios', secondary='func_depart')
    
class RelacionamentoFuncDepart(Base):
    __tablename__ = "func_depart"
    id_departamento = Column(Integer, ForeignKey("departamento.id"), primary_key=True)
    id_funcionario  = Column(Integer, ForeignKey("funcionarios.id"), primary_key=True)
    id_cargo   = Column(Integer, ForeignKey("cargo.id"), primary_key=True)
    departamento = relationship(Departamentos, backref=backref("departamento_assoc"))
    funcionario = relationship(Funcionarios, backref=backref("funcioario_assoc"))
    cargo = relationship(Cargo, backref=backref("cargo_assoc"))

try:
    tables = ["func_depart","cargo","funcionarios", "departamento"]
    sql_cmds = ["drop table if exists orm.%s cascade" % (table) for table in tables]
    for cmd in sql_cmds:
        engine.execute(cmd)
    print ("Tables were dropped with success")
except Exception as error:
    print ("Error while drop tables: %s" % error)

Base.metadata.create_all(engine)
print("Tables recreated")

session = sessionmaker()
session.configure(bind=engine)
s = session()

# Add employee
#funcs = [Funcionarios(nome="Franz Kafka"), Funcionarios(nome="Fiódor Dostoiévsk")]
func = Funcionarios(nome="Franz Kafka")

# Add employee to their department
departamento_1 = Departamentos(nome="Publish House")
#[departamento_1.funcionarios.append(func) for func in funcs]
#s.add(departamento_1)

# Function
cargo = Cargo(nome="Writer")

link = RelacionamentoFuncDepart(departamento=departamento_1, cargo=cargo, funcionario=func)
s.add(link)
s.commit()