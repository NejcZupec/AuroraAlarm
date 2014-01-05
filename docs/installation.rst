
Installation
============

How to setup a development environment
--------------------------------------

Here are the instructions, how to setup a development environment.

The following **prerequisites** are required to run AuroraAlarm:

- Python 2.7
- Virtualenv
- Pip (1.0+)

*Note: we are assuming that you are running an UNIX-like operating system.*

Create a new virtual environment and activate it::

    virtualenv --distribute env
    source env/bin/activate

Clone the repository from Github::

    git clone git@github.com:Gupi/AuroraAlarm.git

Change directory to AuroraAlarm and install all the requirements::

    cd AuroraAlarm
    pip install -r requirements.txt

Synchronize the database and django application. The wizard will ask you to create a new superuser. Create it!::

    cd aurora_alarm
    python manage.py syncdb

Load initial database objects::

    python manage.py loaddata initial_data

Now you are ready to run application::

    python manage.py runserver

Open a web browser and go to::

    http://127.0.0.1:8000

That's it, you have successfully installed AuroraAlarm application :)

How to deploy AuroraAlarm application to Heroku
-----------------------------------------------
