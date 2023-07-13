# DATA STRUCTURES with FLASK API
## Description
- Following Youtube tutorial series to practice Data Structres in real-world application usage.

## Notes 
- ORM (e.g: sqlalchemy) convert object-oriented code into sql statements in query.
    - Tables as `Classes`.
    - 

**Linked List**
- Comment if statement
    - I think below if statement is for the first time running this func because at the initial state, we assign None to last node and nothing modify. If we run again, we knew what's last node , so go to else statement.
    - yeah , we can comment it out after modify in insert_beginning func

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
- Install faker to generate dummy data
```cmd
pip3 install faker
```
## References
- How to work with sqlite db