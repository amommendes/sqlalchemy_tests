from models.company import *
from sqlalchemy.orm import sessionmaker
# Create Engine
engine = connect_db()
Base.metadata.bind = engine

# Create a session configured to engine
DBSession = sessionmaker(bind=engine)
# This is the session itself
s = DBSession()

amom = Funcionarios(nome="Amom Mendes")
it_department = Departamentos(nome="Information Technology")
amom.departamento = it_department

s.add(amom)
s.add(it_department)
s.commit()

it_people = s.query(Departamentos).filter(Departamentos.nome == it_department.nome).one()

for person in it_people.funcionarios:
    print ("Person name fom IT Department: %s" % (person.nome))
