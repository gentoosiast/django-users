#!/bin/sh 

mysql -u root -e "DROP DATABASE askdb"
mysql -u root -e "CREATE DATABASE askdb CHARACTER SET utf8 COLLATE utf8_general_ci"
mysql -u root -e "GRANT ALL PRIVILEGES ON askdb.* TO 'askuser'@'localhost'"
