# gdg_website_backend
GDG Kozhikode - Community Website Backend

# Setup
* Start postgres

* create db with name website
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
# Admin Theme loader - (default:django)
* Bootstrap
```bash
python manage.py loaddata admin_interface_theme_bootstrap.json --settings=config.settings.local
```
* Foundation
```bash
python manage.py loaddata admin_interface_theme_foundation.json --settings=config.settings.local
```
* U.S. Web Design Standards 
```bash
python manage.py loaddata admin_interface_theme_uswds.json --settings=config.settings.local
```