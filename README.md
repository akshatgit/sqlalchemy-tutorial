## Dev Setup
 - Install Virtualenv
 ```bash
 sudo pip3 install virtualenv
 ```
 - Create virtualenv folder
 ```bash
python3 -m venv env
 ```
 Activate Virtualenv
 ```bash
 source env/bin/activate
 ```
 Install requirements
 ```bash
 pip3 install -r requirements.txt
 ```
 Deactivate Virtualenv
 ```bash
deactivate
```
## Run Server
```shell
python server.py
```

## Populate DB
```shell
python populate_db.py
```

# Seeing all Data
```
flask shell
from models.models import Student
Student.query.all()
Student.query.filter_by(name='Akshat').all()
Student.query.get(3)
```
