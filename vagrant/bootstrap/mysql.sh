#!/usr/bin/env bash

# apt-get update -y
DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server mysql-client libmysqlclient-dev python-mysqldb
mysql -u root -e "CREATE DATABASE app DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"
mysql -u root -e "CREATE USER 'app'@'localhost' IDENTIFIED BY 'app';"
mysql -u root -e "CREATE USER 'app'@'10.0.2.2' IDENTIFIED BY 'app';"
mysql -u root -e "GRANT ALL PRIVILEGES ON app.* TO 'app'@'localhost';"
mysql -u root -e "GRANT ALL PRIVILEGES ON app.* TO 'app'@'10.0.2.2';"
# mysql -u root app < /vagrant_data/vagrant/app.sql

sudo cp /etc/mysql/my.cnf /etc/mysql/my.cnf_org
echo "Updating mysql configs in /etc/mysql/my.cnf."
sudo sed -i "s/.*bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
echo "Updated mysql bind address in /etc/mysql/my.cnf to 0.0.0.0 to allow external connections."

sudo service mysql stop
sudo service mysql start
