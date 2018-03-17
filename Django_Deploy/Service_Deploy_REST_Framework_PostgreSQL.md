#### Installing Django Rest Framework with PostgreSQL on Ubuntu 14.04 

## Setting Python Version 
```
alias python='usr/bin/python3.4'
. ~/.bashrc
python --version
```
## Installing PostgreSQL (9.3.11)
```
sudo apt-get install postgresql
sudo apt-get install pgadmin3
sudo passwd postgres
sudo su postgres
sudo service postgresql restart
```
## Setting PostgreSQL
```
vi etc/postgresql/9.3/main/postgresql.conf
listen_addresses = '*'
password_encryption = on
```
```
vi /etc/postgresql/9.3/main/pg_hba.conf
host all all 0.0.0.0/0 password
```
## Installing Django
# djangorestframework 3.3.3
```
sudo apt-get install python-pip
sudo pip install django==1.9.2
sudo apt-get build-dep python-psycopg2
sudo pip install psycopg2
sudo pip install djangorestframework
sudo pip install markdown     
sudo pip install django-filter 
```
## Installing Apache Server
```
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
```
## Setting Django

```
cd /var/www
sudo django-admin.py startproject helloworld
vi /var/www/helloworld/helloworld/views.py
```
```
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello World")
```
```
vi /var/www/helloworld/helloworld/urls.py
```
```
from django.conf.urls import patterns, include, url
from helloworld.views import index

urlpatterns = patterns('',
     url(r'^$', index),
)
```
## Setting Apache Sites-available
```
vi /etc/apache2/sites-available/000-default.conf
```
```
<VirtualHost *:80>
ServerName yourVmName
</VirtualHost>
WSGIScriptAlias / /var/www/helloworld/helloworld/wsgi.py
WSGIPythonPath /var/www/helloworld
```
```
sudo service apache2 restart
```
