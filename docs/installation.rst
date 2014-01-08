
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
Our application is at the moment hosted at Heroku. You can find it here: http://aurora-alarm.herokuapp.com. Sometimes it
takes a couple of seconds to show up, because Heroku stops inactive websites and server needs some time to return a website.

First deploy
^^^^^^^^^^^^
Let's assume you want to deploy application for the first time. First you have to register at Heroku and setup an environment.
You can follow this simple quickstart tutorial: https://devcenter.heroku.com/articles/quickstart. After step 3 follow our
instructions bellow.

*Note: we are assuming that you are running an UNIX-like operating system.*

Create a new directory, e.g. name it aurora-alarm::

    mkdir aurora-alarm && cd aurora-alarm

Create Procfile for a your new app and enter command starting gunicorn server. Check if the name of application is correct::

    echo web: gunicorn aurora-alarm.wsgi > Procfile

Clone the latest code from Github somewhere to your disk::

    cd ..;git clone git@github.com:Gupi/AuroraAlarm.git

Copy all file from the folder aurora-alarm (from cloned repository) to your created repository for Heroku. All files should be
in root of your repository::

    cp AuroraAlarm/aurora-alarm aurora-alarm

Now we have to replace some files which are important for Heroku. In our Github repository you can find deploy folder, where
you will find all the important files for Heroku, which are a bit different than the files in development version of the code::

    cp AuroraAlarm/deploy/requirements.txt aurora-alarm
    cp AuroraAlarm/deploy/settings.py aurora-alarm/aurora-alarm
    cp AuroraAlarm/deploy/wsgi.py aurora-alarm/aurora-alarm

Ok, all files and directory structure is now prepared for deployment to Heroku. Create a new git repository and commit
all the files::

    git init
    git add *
    git commit -m "Deploy all file to Heroku."

Create a new Heroku app::

    heroku create

Deploy everything to Heroku::

    git push heroku master

Now you have to setup a database through CLI. Run bash::

    heroku run bash

When command line is initialized, you have to run next commands::

    python manage.py syncdb
    python manage.py migrate photologue
    python manage.py syncdb

After first syncdb you will receive an error, because photologue tables are not included. That's why we have to run
migrate command and after a command syncdb one more time.

Well, you have successfully deployed your application to Heroku. Now you can run the deployed application and check if
everything works::

    heroku open

This command will open your browser and you should be able to see running application. If you have any problems, you can
open heroku logs and than you will be able to find a problem::

    heroku logs

Update existing Heroku app
^^^^^^^^^^^^^^^^^^^^^^^^^^

