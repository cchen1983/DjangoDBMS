# Install Project Dependencies:
1. install mysql and configuration: 
    http://dev.mysql.com/doc/refman/5.6/en/installing.html;

2. install python & django & mySQLdb:
    1). Install python 2.7.10
        https://www.python.org/downloads/
        
        Windows: 
        https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi

    2). Install pip:   
        python get-pip.py

        https://pip.pypa.io/en/stable/installing/

    3). pip install django==1.8.4
    4). pip install MySQL-python
    
# Init database(only for mysql environment)
#    mysql -u <username> -p < wakaInit.sql

# Run Waka Web Service:

    1. python manage.py migrate
    2. python manage.py runserver localhost:8000

# Backup and Import data:
    # Backup to file
        python manage.py dumpdata > db.json
    # Load from file
        python manage.py loaddata db.json 
