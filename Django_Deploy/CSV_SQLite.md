##Create dataset
```
( echo 'a,b,c' ; echo '1,2,3' ) > somedata.csv
```
##Import CSV
```
sqlite3 database.sqlite3
.mode csv
.import somedata.csv sometable
```
##Select data
```
SELECT * FROM sometable;
```
##SQL Script Convert SQLite3
```
sqlite3 database.sqlite3 < db.sql
```
