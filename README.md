# Service for managing polls 

# Running:
## step 1: run postgresql in docker container
```docker-compose up db```

## step 2: install requirements
```pip install -r requirements.txt```

## step 3: update the database schema using migrations 
```python manage.py migrate```

## step 4: run django app
```python manage.py runserver <host>:<port>```