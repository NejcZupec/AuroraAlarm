AuroraAlarm
===========
AuroraAlarm is a simple web application for monitoring auroral activity. It consists of four main parts: 

1. **Aurora Activity** - check history and forecast of auroral activity
2. **Aurora Alarms** - set aurora notifications
3. **Aurora Gallery** - upload and share the nicest images of aurora
4. **Aurora Map** - check where you can see the nicest aurora

The basic idea of the application is that you will never miss aurora activity near your location. You can sign up for notifications and when aurora will be active, you will receive an email. At the moment it works just in Europe. 

This project is a part of Design of Dynamic Web Systems course at Luleå University of Technology.

Current stable version is accessible at Heroku: http://aurora-alarm.herokuapp.com/

Installation
------------
Here are the instructions, how to setup a development environment.

The following **prerequisites** are required to run AuroraAlarm:
* Python 2.7
* Virtualenv
* Pip (1.0+)

*Note: we are assuming that you are running an UNIX-like operating system.*

Create a new virtual environment and activate it:
    
    virtualenv --distribute env
    source env/bin/activate
    
Clone the repository from Github:

    git clone git@github.com:Gupi/AuroraAlarm.git
    
Change directory to AuroraAlarm and install all the requirements:

    cd AuroraAlarm
    pip install -r requirements.txt
    
Synchronize the database and django application. The wizard will ask you to create a new superuser. Create it!

    cd aurora_alarm
    python manage.py syncdb

Load initial database objects:

    python manage.py loaddata initial_data

Now you are ready to run application:

    python manage.py runserver
    
Open a web browser and go to:

    http://127.0.0.1:8000

That's it, you have successfully installed AuroraAlarm application :)

Documentation
-------------
The full documentation is accessible on readthedocs.org: <https://auroraalarm.readthedocs.org/>

Requirements
------------
* Python 2.7
* Django 1.6
* Celery 3.1.5
* Python Social Auth 0.1.17
* Django REST Framework 2.3.8

Links
-----
* Documentation: https://auroraalarm.readthedocs.org/
* Course site: https://sites.google.com/a/ltu.se/m7011e-2013/
* Deployed version at Heroku: http://aurora-alarm.herokuapp.com/
* Issues and roadmap: https://github.com/Gupi/AuroraAlarm/issues

Contributors
------------
* Nejc Zupec
* Prisca Bonnet

