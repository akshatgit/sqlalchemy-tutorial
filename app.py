from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

# create a Flask application object and set URI for the database to be used.
app = Flask(__name__, template_folder='templates')
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' 

# init db 
db.init_app(app)

with app.app_context():
    db.create_all()