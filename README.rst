docker run -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -e POSTGRES_DB=root postgres

python3 -m venv venv

pip install --upgrade pip

pip install -r askbot_requirements.txt

pip install psycopg2

pip install 'django-appconf==1.0.3'

# try installing also this
# python -m pip install --upgrade setuptools

python setup.py install --single-version-externally-managed --root=/

askbot-setup --force

# cd into created project

python -m pip install --upgrade setuptools

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080