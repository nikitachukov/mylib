mysql -h localhost -u root < recreate.sql
./manage.py migrate --noinput
./manage.py loaddata auth
./manage.py loaddata stations
./manage.py loaddata genres
