# Deploy Django 1.7 with Python3 on Azure Ubuntu 14.04

## Virtual Environment
### python2
```
sudo apt-get update
sudo apt-get install python-pip apache2 libapache2-mod-wsgi
```
### python3
```
sudo apt-get update
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
```

### Configure Virtual Environment
```
sudo pip install virtualenv
mkdir myproject
cd myproject
virtualenv myprojectenv
source myprojectenv/bin/activate
```

### Create Django Project
```
pip install "django<1.8"
django-admin.py startproject myproject
```
### Add a line to configure this directory.
```
nano myproject/settings.py
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
```
### Complete initial project 
```
cd mysite
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py collectstatic
./manage.py runserver 0.0.0.0:8000
```

## Apache
```
sudo nano /etc/apache2/sites-available/000-default.conf
```
```
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /home/azureuser/myproject

    Alias /static /home/azureuser/myproject/static
    <Directory /home/azureuser/myproject/static>
        Require all granted
    </Directory>
    
    <Directory /home/azureuser/myproject/myproject>
    <Files wsgi.py>
        Require all granted
    </Files>
    </Directory>
    
    WSGIDaemonProcess myproject python-path=/home/azureuser/myproject:/home/user/myproject/myprojectenv/lib/python2.7/site-packages
    WSGIProcessGroup myproject
    WSGIScriptAlias / /home/azureuser/myproject/myproject/wsgi.py
</VirtualHost>
```
```
sudo chmod 664 myproject/db.sqlite3
sudo chown :www-data myproject/db.sqlite3
sudo chown :www-data myproject
sudo service apache2 restart
```
