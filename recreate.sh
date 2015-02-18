mysql -h localhost -p -u root --password=admin4all < recreate.sql
./manage.py migrate --noinput
./manage.py loaddata auth
./manage.py loaddata stations
./manage.py loaddata genres
