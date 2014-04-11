# The Emergency Room Manager: simplER

*An application to simplify hospital emergency rooms*

## dev environment
- Python2.7 / Django 1.6.2 / Ubuntu 12.04

```
	sudo apt-get install python2.7
	sudo apt-get install python-pip
	sudo pip install django

	cd /simpler
	python manage.py syncdb
	python manage.py runserver

```
- `python manage.py syncdb` will create / sync a local database for development
- `python manage.py runserver` will run the development server
- `/simpler` is the actual python project directory
