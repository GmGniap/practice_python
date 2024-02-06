from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine, select
'''
## Tasks
1. [Paing] Get models from Models.py
2. [Paing] Convert models into SQLModel
    1. Get models attributes
    2. Get models types
3. [Paing] Convert models types to SQLModel data types
    1. python default types
4. [HKS] Connection
    1. Db connect
    2. CREATE
    3. READ
    4. UPDATE
    3. DELETE

'''

class SampleStudent(object):
    def __init__(self, fullname:str, age:int):
        self.fullname = fullname
        self.age = age

s = SampleStudent('Test', 12)

class DatabaseManager(object):
    def __init__(self, data_obj) -> None:
        self.data_obj = data_obj
    
    def get_attributes_dataObj(self):
        pass

class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fullname : str
    age : int

s1 = Student(fullname=s.fullname, age=s.age)

engine = create_engine("sqlite:///model.db")

SQLModel.metadata.create_all(engine)
with Session(engine) as session:
    session.add(s1)
    session.commit()