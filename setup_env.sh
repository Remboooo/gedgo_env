virtualenv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt

python manage.py syncdb
python manage.py migrate
