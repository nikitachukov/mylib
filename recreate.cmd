"c:\Program Files\MySQL\MySQL Server 5.6\bin\mysql" -h localhost -u root -p < recreate.sql
manage.py migrate --noinput
manage.py loaddata auth
manage.py loaddata stations
manage.py loaddata genres