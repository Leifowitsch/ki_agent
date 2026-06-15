from sqlmodel import SQLModel, create_engine, Session
from models import 

engine = create_engine("sqlite:///databse.db")

def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        new_entry = 

