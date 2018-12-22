from models.model import *
from models.company import *

engine = connect_db()
Base.metadata.create_all(engine)