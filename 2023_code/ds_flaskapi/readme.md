# DATA STRUCTURES with FLASK API
## Description
- Following Youtube tutorial series to practice Data Structres in real-world application usage.

## Notes 
- ORM (e.g: sqlalchemy) convert object-oriented code into sql statements in query.
    - Tables as `Classes`.
    - 

## Error
- While creating sqlite file in python terminal , it's showing error for "Working outside of application context."
    - To solve that , run with below command.
```
>>> from server import app, db
>>> with app.app_context():
        db.create_all()
```

## Installation
- Install Flask
```cmd
pip3 install Flask
```
- Install SQLAlchemy
```cmd
pip3 install SQLAlchemy
```
- Install flask-sqlalchemy
```cmd
pip3 install flask-sqlalchemy
```
## References
- How to work with sqlite db