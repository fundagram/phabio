docker run --name magento2_db -d -e MYSQL_ROOT_PASSWORD="rootpassword" -e MYSQL_DATABASE="magento2" -e MYSQL_USER="user" -e MYSQL_PASSWORD="password" mysql
docker run --name magento2_web -d -p 80 --link=magento2_db:db chadrien/magento2:5.6-apache-full-1.0.0-beta
docker port magento2_web
