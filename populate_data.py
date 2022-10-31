import json
from app import db, app
from models.models import Student

def populate_data():    
    with open('data.json') as f:
        data = json.load(f)
    
    # create db if not exists
    with app.app_context():
        db.create_all()

    app.app_context().push()
    
    students = data["students"]
    for student in students:
        name = student["name"]
        pin = student["pin"]
        city = student["city"]
        addr = student["addr"]
    
        new_student = Student(name = name, city=city, addr = addr, pin = pin)

        # To add this student to the database, you’ll first need to add it to 
        # a database session, which manages a database transaction.
        db.session.add(new_student)

    # To commit the transaction and apply the change to database,
    # use the db.session.commit() method:
    db.session.commit()

if __name__ == '__main__':
    populate_data()   
    