#!/usr/bin/env python

import sys
sys.dont_write_bytecode = True

try:
    import mysql.connector
except ImportError as e:
    print(str(e))
    print('Try...')
    print('    redhat install: yum install mysql-connector-python')
    print('    debian install: apt-get install python-mysql.connector')
    sys.exit(1)

try:
    import config
except ImportError as e:
    print('Missing config.py: ' + str(e))
    sys.exit(1)
dbSocket = config.gclid['dbSocket']
dbUser = config.gclid['dbUser']
dbPass = config.gclid['dbPass']

try:
    config = {
        'user': dbUser,
        'password': dbPass,
        'unix_socket': dbSocket,
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

sql =  "SELECT main.tbl_customer.gclid, nic_billing.order.order_date "
sql += "FROM main.tbl_customer INNER JOIN nic_billing.order "
sql += "ON nic_billing.order.id_customer = main.tbl_customer.CUSTOMER_ID "
sql += "WHERE main.tbl_customer.gclid IS NOT NULL "
sql += "AND nic_billing.order.order_status = 'success' "
sql += "AND nic_billing.order.order_date >= (CURDATE() - INTERVAL 31 DAY) "
sql += "ORDER BY nic_billing.order.order_date ASC "
#sql += "LIMIT 5"

cursor = cnx.cursor(buffered=True)
try:
    cursor.execute(sql)
    if cursor.rowcount > 0:
        get_results = cursor.fetchall()
    else:
        get_results = ''

except Exception as e:
    print(str(e))
    sys.exit(1)

cursor.close()
cnx.close()

# work with the data...
# we have get_results fetchall()/list
#for row in get_results:
#    print(row)

print("Google Click ID,Conversion Name,Conversion Time,Conversion Value,Conversion Currency")
for (gclid, order_date) in get_results:
    #print(row)
    print("{},15-day ELTV adjustment,{:%Y-%m-%d %H:%M:%S} America/Los_Angeles,partner.vertical_type,USD".format(gclid, order_date))

sys.exit(0)
