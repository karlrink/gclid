# gclid

# Upload Offline Customer Conversions To Google Using GCLID 


# https://nationsinfocorp.atlassian.net/browse/ENG-2275

##################################################################################################
# install/setup

requires python-mysql.connector    

current system has python 2...    
python-mysql.connector - pure Python implementation of MySQL Client/Server protocol        
python3-mysql.connector - pure Python implementation of MySQL Client/Server protocol (Python3)    

debian install:
```
$ apt-get install -y python-mysql.connector
```

##################################################################################################

# dbUser...
```
# mysql 8

mysql> create ROLE 'gclid_role';
mysql> grant select on main.tbl_customer TO 'gclid_role';
mysql> grant select on nic_billing.order TO 'gclid_role';

mysql> create user 'gclid'@'localhost' IDENTIFIED WITH mysql_native_password BY 'XXXXXXXX';
mysql> grant 'gclid_role' to 'gclid'@'localhost';

```


