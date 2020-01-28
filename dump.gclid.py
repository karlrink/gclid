#!/usr/bin/env python

import sys
import os

dbConf = 'db.conf'
dbUser = dbPass = None
mysql_socket = '/var/run/mysqld/mysqld.sock'

try:
    with open(dbConf) as Conf:
        for line in Conf:
            if line.startswith("define('dbUser'"):
                dbUser = line.split(',')[1].strip('\'').split('\'')[0]
            if line.startswith("define('dbPass'"):
                dbPass = line.split(',')[1].strip('\'').split('\'')[0]
except Exception as e:
    print(e)
    sys.exit(1)

try:
    import mysql.connector
except ImportError as e:
    print(str(e))
    print('Try...')
    print('    redhat install: yum install mysql-connector-python')
    print('    debian install: apt-get install python-mysql.connector')
    sys.exit(1)

try:
    config = {
        'user': dbUser,
        'password': dbPass,
        'unix_socket': mysql_socket,
        'database': '',
        'raise_on_warnings': True,
        'auth_plugin': 'mysql_native_password',
    }
except Exception as e:
    print(str(e)) 
    sys.exit(1)

try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print(str(e))
    sys.exit(1)


cursor = cnx.cursor(buffered=True)

try:
    sql = "show status;"
    cursor.execute(sql)
    if cursor.rowcount > 0:
        show_status = cursor.fetchall()
    else:
        show_status = ''

except Exception as e:
    print(str(e))

cursor.close()
cnx.close()

#work with the data...
# we have show_status fetchall()/list
for row in show_status:
    print(row)


#basic setup done... continue this tomorrow...
