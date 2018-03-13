# gdg_website_backend
GDG Kozhikode - Community Website Backend

# Setup
* Start postgres 

* create db with name _website_
```bash
$ psql
$ CREATE DATABASE website;
$ \q
```
* Create a virtualenv(with wrapper) with python3
```bash
$ mkvirtualenv -p python3 gdg    
```
* cd into the project folder
```bash
$ cd website
```
* Install requirements
```bash
$ pip install requirements/local.txt
```
* Create super-user
```bash
$ python manage.py createsuperuser --settings=config.settings.local
```
* Migate database
```bash
$ python manage.py migrate --settings=config.settings.local
```
* Creating the admin interface assets
```bash
$ python manage.py collectstatic --settings=config.settings.local
```
* Dumping the dummy DB data
```bash
$ python manage.py loaddata db.json --settings=config.settings.local
```
* Run the server (*Make sure postgres server is running*)
```bash
$ python manage.py runserver_plus --settings=config.settings.local
```

# Using the admin panel
*http://127.0.0.1:8000/admin/*

### Login credentials
_username_ : **demo** <br>
_password_ : **gdgkozhikode**
