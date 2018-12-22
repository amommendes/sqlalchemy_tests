from models.model import Base, Pessoa, Endereco, connect_db
from sqlalchemy.orm import sessionmaker
# Create Engine
engine = connect_db()
Base.metadata.bind = engine

# Create a session configured to engine
DBSession = sessionmaker(bind=engine)
# This is the session itself
session = DBSession()

pessoas = [Pessoa(nome=pessoa) for pessoa in ["Michele Mendes Luiz", "Maria", "Alberto"]]
amom = Pessoa(nome="Amom Mendes Luiz")
session.add(amom)
session.add_all(pessoas)
endereco_amom = Endereco(nome_rua="170 9th Avenue SW", numero="2100", pessoa=amom)
session.add(endereco_amom)

try:
    session.commit()
except Exception as error:
    session.rollback()
    print(error)