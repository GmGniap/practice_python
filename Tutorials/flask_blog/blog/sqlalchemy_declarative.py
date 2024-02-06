from sqlalchemy.orm import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.dialects.sqlite import insert
Base = declarative_base()
engine = create_engine("sqlite:///model.db")

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

Base.metadata.create_all(engine)

Session = sessionmaker(bind= engine)
session = Session()

class SampleStudent(object):
    def __init__(self, fullname:str, age:int):
        self.fullname = fullname
        self.age = age

# s1 = SampleStudent("Test3", 20)  
# ## Insert Student Data
# stu = Student("Test3", )

# session.add(stu)
# session.commit()

## Insert Tutor Data - 
with engine.connect() as conn:
    insert_statement = insert(Student).values([90, 'Test6', 70]).on_conflict_do_nothing()
    conn.execute(insert_statement)
    conn.commit()
