from flask import render_template, request, flash, redirect, url_for
from models.models import Student
from app import app, db
# db.create_all()

# import models

# create / path
@app.route('/')
def show_all():
   return render_template('show_all.html', students = Student.query.all())

# create /new path
@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         student = Student(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])
         
         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

app.run(debug = True)