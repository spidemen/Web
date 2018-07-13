OS: AWS linux
Database: Mysql
Web server: Apache
Web page: html
Backend: Django
Install Packges: python version 3.5.2  apache2, mod_python,django, mysql-server, mysql-client, libmysqlclient-dev, python-dev, python-mysqldb, libapache2-mod-python
After install libapache2-mod-python, then 
sudo ln -s /etc/apache2/mods-available/python.load /etc/apache2/mods-enabled/
Configuration mod_python:
Create python.conf in directory /etc/apache2/mods-available/
sudo vi /etc/apache2/mods-available/python.conf
Add following content:
<Directory /var/www>
    AddHandler mod_python .py #a space needed
    PythonHandler test
    PythonDebug On
</Directory>
Then save, then 
sudo ln -s /etc/apache2/mods-available/ python.conf /etc/apache2/mods-enabled/

After install django, create a projection:
django-admin.py startproject mysite  (then you just needed to replace this director with my after some configuration )
run:
python manage.py runserver 0.0.0.0:8000

Putting django into apache2:
Open /etc/apache2/sites-available/default configuration file modify following:
DocumentRoot /home/bill/Desktop/source_code/web/mysite    # mysite directory
Then restart apache2
The above is introduction how to build environment.
After you successful building  environment, then you should modify mystic/mysite/setting.py
Find database setting content, then fill you database basic information like database name, password, username, port.
In our project, we use userdb as database name, main table introduce in the report.

Besides, we have our own website on AWS.
Website address: http://54.183.168.96:8000/insert/
http://54.183.168.96:8000/insert/ this link would show all the information of user
Directory Introduce:
Djang_web--- Django application 
Mysite-----default application/Users/xing/Desktop/课件/ECE 524 fundamental of cloud computing/project/mysite/readme.txt
Templates: html web page code
How to run this website?? Just use that website address to access by http web browser
Or  just install apache +Django+mysql then create mysite app, then replace mystic directory with my mysite. If want to run locally, then you should use address like 127.0.0.0:8000/insert/. 
Notice: when you want to run website, you should type command like python manage.py runserver 0.0.0.0:8000. I recommend that you just use our website to test or you will meet a lot of bug when you build environment.
If you want to login our VM, you can send e-mail to us. We will send you a encryption file to you, which is useful for ssh logging.

Django_web: views.py  code for tacking requst from web
	    Models.py.  Just for database, create model for database tables
Mysite: urls.py configuration url 
	settings.py.  app ,database configuration

Templates:
	insert.html. insert page, main login page
	signup.html   signup page
	admin1.html.  admin login page
	show.html.    show all user information page
