from models.model import Base, Pessoa, Endereco, connect_db
from sqlalchemy.orm import sessionmaker
# Create Engine
engine = connect_db()
Base.metadata.bind = engine

# Create a session configured to engine
DBSession = sessionmaker(bind=engine)
# This is the session itself
session = DBSession()

pessoa = session.query(Pessoa).first()
print("First database person: %s" % (pessoa.nome))
endero_da_primeira_pessoa = session.query(Endereco).filter(Endereco.pessoa == pessoa).one()
print("Adress from the first database person: %s" % (endero_da_primeira_pessoa.nome_rua))
