
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

Django has a model-view-controller (MVC) architecture:
 * Model: in model we defined all objects important for
 * View: here we prepared different HTML5/CSS3 templates, built with Twitter Bootstrap framework.
 * Controller: logic part of the application

**Celery and Queue**

**PostgreSQL or SQLite**

Client side
-----------
**Web browser**


TODO: A description of your software parts and how they interact with each other.
