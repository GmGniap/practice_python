from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
import data_structures.linked_list as ll

## BTS: WSGI app works as middleware between Python app and server. 
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dsadb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0    ## what it's doing?

# configure sqlite3 to enforce foreign key constraints
# what's SQLite default 
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()
    
db = SQLAlchemy(app)
now = datetime.now()

# models (tables as classes)
## table classes inherited with db.Model class
class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    events = db.relationship("Event", cascade="all, delete")

class Event(db.Model):
    __tablename__ = "event_table"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    details = db.Column(db.String(200))
    date = db.Column(db.Date)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)

# routes
@app.route("/student", methods= ["POST"])
def create_student():
    ## request provided by Flask and it contains payload(like dict object)
    data = request.get_json()
    new_student = Student(
        name = data['name'],
        email = data['email'],
        address = data['address'],
        phone = data['phone'],
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student created"}), 200

@app.route("/student/descending_id", methods=["GET"])
def get_all_students_descending():
    students = Student.query.all()
    all_students_ll = ll.LinkedList()
    
    for student in students:
        all_students_ll.insert_beginning(
            {
                "id":student.id,
                "name":student.name,
                "email":student.email,
                "address":student.address,
                "phone":student.phone
            }
        )
    return jsonify(all_students_ll.to_list()), 200

@app.route("/student/ascending_id", methods=["GET"])
def get_all_students_ascending():
    students = Student.query.all()
    all_students_ll = ll.LinkedList()
    
    for student in students:
        all_students_ll.insert_at_end(
            {
                "id":student.id,
                "name":student.name,
                "email":student.email,
                "address":student.address,
                "phone":student.phone
            }
        )
    return jsonify(all_students_ll.to_list()), 200

@app.route("/student/<student_id>", methods=["GET"])
def get_one_student(student_id):
    students = Student.query.all()
    all_students_ll = ll.LinkedList()
    
    for student in students:
        all_students_ll.insert_beginning(
            {
                "id":student.id,
                "name":student.name,
                "email":student.email,
                "address":student.address,
                "phone":student.phone
            }
        )
    user = all_students_ll.get_student_by_id(student_id)
    if user is None:
        return jsonify({"message": "Not found."}), 200
    return jsonify(user), 200

@app.route("/student/<student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = Student.query.filter_by(id=student_id).first()
    if app.app_context():
        db.session.delete(student)
        db.session.commit()
    return jsonify({}),200

@app.route("/event/<student_id>", methods=["POST"])
def create_event(student_id):
    pass

@app.route("/student/<student_id>", methods=["GET"])
def get_all_events(student_id):
    pass


if __name__ == "__main__":
    app.run(port= 8000, debug=True)


