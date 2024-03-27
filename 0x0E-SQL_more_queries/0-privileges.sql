#!/bin/bash

# MySQL credentials
MYSQL_USER="your_mysql_username"
MYSQL_PASSWORD="your_mysql_password"

# MySQL database
MYSQL_DB="mysql"

# MySQL users to check privileges for
USERS=("user_0d_1" "user_0d_2")

# Loop through each user and fetch privileges
for USER in "${USERS[@]}"; do
    echo "Privileges for user: $USER"
    mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW GRANTS FOR '$USER'@'localhost';" "$MYSQL_DB"
    echo "----------------------------------"
done
