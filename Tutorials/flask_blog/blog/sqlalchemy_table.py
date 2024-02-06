from sqlalchemy import Table, Column, Integer, String, create_engine, MetaData
from sqlalchemy.orm import Session
from sqlalchemy.orm import registry
from sqlalchemy.dialects.sqlite import insert

mapper_registry = registry()

metadata_obj = MetaData()

studentTable = Table(
    "student_table",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("fullname", String),
    Column("age", Integer)
)


class SampleStudent(object):
    def __init__(self, fullname:str, age:int):
        self.fullname = fullname
        self.age = age

mapper_registry.map_imperatively(SampleStudent,studentTable)

engine = create_engine("sqlite:///model.db")

def create_table(table_name:str, engine , schema:str):
    # metadata = MetaData(schema=schema)
    table = Table(table_name, metadata_obj, autoload_with=engine, schema = schema)
    metadata_obj.create_all(engine)
    return table

def insert_batch(table, batch:list, conn):
    insert_statement = insert(table).values(batch).on_conflict_do_nothing()
    conn.execute(insert_statement)
    conn.commit()
    
def main():
    s = SampleStudent('Test', 12)
    metadata_obj.create_all(engine)
    with Session(engine) as session:
        session.add(s)
        session.commit()

# def main():
#     s = SampleStudent('Test', 12)
#     table = create_table(table_name="student", engine=engine , schema="model")
#     with engine.connect() as conn:
#         conn.execute(
#             insert(table)
#             .values([s.fullname, s.age])
#         )
        
#         conn.commit()


    
if __name__ == "__main__":
    main()
    