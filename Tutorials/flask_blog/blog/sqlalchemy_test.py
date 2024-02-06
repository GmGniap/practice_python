from sqlalchemy.orm import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.dialects.sqlite import insert

class DatabaseManager(object):
    def __init__(self) -> None:
        self.Base = declarative_base()
        self.engine = create_engine("sqlite:///model.db")

## Declarative class
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    age = Column(Integer)

## Imperative 
tutorTable = Table(
    "tutor_table",
    Base.metadata,
    Column("fullname", String),
    Column("age", Integer)
)

def create_tables():
    Base.metadata.create_all(engine)

Session = sessionmaker(bind= engine)
session = Session()

## Insert Student Data
stu = Student(fullname="Test2", age= 25)

session.add(stu)
session.commit()

## Insert Tutor Data
with engine.connect() as conn:
    insert_statement = insert(tutorTable).values(['Tutor', 40]).on_conflict_do_nothing()
    conn.execute(insert_statement)
    conn.commit()
