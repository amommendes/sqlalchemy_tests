from models.model import Base, Pessoa, Endereco, connect_db
from sqlalchemy.orm import sessionmaker
# Create Engine
engine = connect_db()
Base.metadata.bind = engine

# Create a session configured to engine
DBSession = sessionmaker(bind=engine)
# This is the session itself
session = DBSession()

person = session.query(Pessoa).first()
print("First database person: %s" % (person.nome))
adress_from_first_person = session.query(Endereco).filter(Endereco.pessoa == pessoa).one()
print("Adress from the first database person: %s" % (adress_from_first_person.nome_rua))
