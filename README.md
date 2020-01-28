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

##################################################################################################
# output
```
### INSTRUCTIONS ###,,,,
"# IMPORTANT: Remember to set the TimeZone value in the ""parameters"" row and/or 
in your Conversion Time column",,,,
# For instructions on how to set your timezones visit http://goo.gl/T1C5Ov,,,,
,,,,
### TEMPLATE ###,,,,
Parameters:TimeZone=America/Los_Angeles
Google_Click_ID,Conversion_Name,Conversion_Time,Conversion_Value,Conversion_Currency
```

Conversion Time: the date and time that the conversion occurred, example,
```
yyyy-MM-ddTHH:mm:ss zzzz | "2012-08-14T13:00:00 America/Los_Angeles"

```

example...
```
Cj0KCQiAiNnuBRD3ARIsAM8KmlsWutPbDFd5lmMUtyDOuQrEv5IlJKgnSFqqV1qu4kTizFf54XtBynEaArErEALw_wcB,15-day ELTV adjustment,2012-08-14 13:00:00 America/Los_Angeles,partner.vertical_type,USD
```




