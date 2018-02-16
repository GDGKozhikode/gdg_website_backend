# gdg_website_backend
GDG Kozhikode - Community Website Backend

# Setup
* Start postgres
```bash
$ psql
```
* create db with name website
```bash
$ CREATE DATABASE website;
$ \q
```
* Migate to database
```bash
$ python manage.py migrate --settings=settings.local
```
* Creating the admin interface assets
```bash
$ python manage.py collectstatic --settings=settings.local
```
# Theme loader - (default:django)
* Bootstrap
```bash
python manage.py loaddata admin_interface_theme_bootstrap.json --settings=settings.local
```
* Foundation
```bash
python manage.py loaddata admin_interface_theme_foundation.json --settings=settings.local
```
* U.S. Web Design Standards 
```bash
python manage.py loaddata admin_interface_theme_uswds.json --settings=settings.local
```