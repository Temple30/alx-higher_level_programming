#!/bin/bash

# MySQL credentials
MYSQL_USER="your_mysql_username"
MYSQL_PASSWORD="your_mysql_password"

# MySQL user details
USER="user_0d_1"
PASSWORD="user_0d_1_pwd"

# MySQL database
MYSQL_DB="mysql"

# Check if the user already exists
EXISTING_USER=$(mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SELECT user FROM mysql.user WHERE user='$USER';" "$MYSQL_DB" | grep "$USER")

# If the user exists, update its privileges
if [ ! -z "$EXISTING_USER" ]; then
    echo "User $USER already exists. Updating privileges..."
    mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SET PASSWORD FOR '$USER'@'localhost' = PASSWORD('$PASSWORD');" "$MYSQL_DB"
    mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "GRANT ALL PRIVILEGES ON *.* TO '$USER'@'localhost' WITH GRANT OPTION;" "$MYSQL_DB"
    echo "Privileges updated for user $USER."
else
    # Create user with all privileges
    echo "Creating user $USER..."
    mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "CREATE USER '$USER'@'localhost' IDENTIFIED BY '$PASSWORD';" "$MYSQL_DB"
    mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "GRANT ALL PRIVILEGES ON *.* TO '$USER'@'localhost' WITH GRANT OPTION;" "$MYSQL_DB"
    echo "User $USER created with all privileges."
fi
