python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r askbot_requirements.txt

pip install psycopg2

pip install 'django-appconf==1.0.3'

python setup.py install --single-version-externally-managed --root=/

cd recovenn

python manage.py runserver 0.0.0.0:8080
