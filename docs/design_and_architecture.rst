
Design and Architecture
=======================

Our application is a typical client-server application. We have provided a scheme bellow, where you can see the most
important parts of the application. We have two set-ups, development version and version for Heroku. If you want to
install or deploy this application, read the instructions in *Installation* chapter.

.. image:: img/aurora_alarm_diagram.png

Further description is written for a deployed version at Heroku.

Server side
-----------
**Django server (Gunicorn)**
  This server contains Django framework. Django has a model-view-controller (MVC) architecture:
 * Model: in model we defined all objects. Above model there is RESTful API, created with Django REST Framework. All ajax calls from web browsers go through API.
 * View: here are different HTML5/CSS3 templates, built with Twitter Bootstrap framework.
 * Controller: logic part of the application is simplified. The main logic is actually moved to JavaScript/jQuery scripts and is loaded in browsers.

**Celery and Queue**
  AuroraAlarm has a lot of background/asynchronous jobs. These jobs are performed with Celery, an asynchronous task queue. For example: sending emails, alerting, calculating distances, etc. At the moment we haven't implemented all backend tasks yet, but we prepared everything for further development.

**PostgreSQL or SQLite**
  Data is stored in PostgreSQL (deployed version at Heroku) or SQLite (development version). Django uses Object-relational mapping (ORM) and supports all well-known databases. If you want to switch between different databases, you just have to set correct settings in settings.py file, which you can find it in aurora_alarm/aurora_alarm folder.

Client side
-----------
**Web browser**
  When browser makes first request, it receives HTML content and JavaScript/jQuery scripts. In these scripts is written a main logic of the application. All data from database is collected with AJAX calls through API.

Files structure
---------------
Our project has a recommended Django file structure. Here is a short description for each directory:

* **aurora_alarm**:
    * **api**: application for REST api needs
    * **aurora_alarm**: main urls router, context processor and celery settings
    * **frontend**: graphical user interface for a web application, static files
    * **templates**: HTML5/CSS3 templates created with Twitter Bootstrap
* **deploy**: all files which are necessary for deployment to Heroku
* **docs**: documentation files created with Sphinx
