all: install migrate start

install:
	pip3 install -r requirements.txt

test:
	python3 manage.py test

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

create_admin:
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python3 manage.py shell

start:
	python3 manage.py runserver

