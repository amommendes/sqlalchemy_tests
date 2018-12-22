from models.model import *

engine = connect_db()
Base.metadata.create_all(engine)