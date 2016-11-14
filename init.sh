#!/bin/sh

sudo /etc/init.d/mysql restart
mysql -u root -e "CREATE USER 'askuser'@'localhost' IDENTIFIED BY 'simplepass'"
mysql -u root -e "CREATE DATABASE askdb CHARACTER SET utf8 COLLATE utf8_general_ci"
mysql -u root -e "GRANT ALL PRIVILEGES ON askdb.* TO 'askuser'@'localhost'"
sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /home/box/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -s /home/box/etc/gunicorn.conf /etc/gunicorn.d/django
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
python2 /home/box/web/ask/manage.py syncdb
