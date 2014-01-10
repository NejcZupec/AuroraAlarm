
Technology Stack
================

AuroraAlarm is built with quite new and popular, open source technologies. In this project we wanted to learn and try, how to use
all these technologies and how they interact between each other. Further we would like to list all technologies we have used
and write a short description for each, why we have chosen it.

Backend
-------
**Django** (https://www.djangoproject.com/)
  Django is a high-level Python web framework. We have chosen it, because it is Python based, you can write fast, you don't have to repeat yourself and it has a really good documentation.
**Django REST Framework** (http://www.django-rest-framework.org/)
  Django REST framework is a powerful and flexible toolkit that makes it easy to build Web APIs. It has a really good web browseable API which can help you, when you develop API. Documentation is also very good and community is active.
**Django Photologue gallery** (https://github.com/jdriscoll/django-photologue)
  A powerful image management and gallery application for the Django web framework. You can upload photos, group them into galleries, apply effects such as watermarks. We have chosen it, because it is highly customizable and easy to integrate.
**Celery** (http://www.celeryproject.org/)
  Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well. All our backend jobs are executed with celery: sending emails, collecting aurora forecast data, alerting system,...
**Highcharts API** (http://www.highcharts.com/)
  Highcharts is a charting library written in pure HTML5/JavaScript, offering intuitive, interactive charts to your web site or web application. We used this library at aurora history/forecast chart. We have decided for it, because it is for free and at the moment very popular library for drawing different charts.
**Gunicorn** ()
  Server running Django-based applications.

Graphical User Interface
------------------------
**Twitter Bootstrap** (http://getbootstrap.com/)
  Bootstrap is sleek, intuitive, and powerful mobile first front-end framework for faster and easier web development. It is purely written in HTML5/CSS3. This framework is the most popular project at Github at the moment. Nowadays a lot of web pages looks very similar, because of Bootstrap popularity. That's why we have decided to buy a prepared theme, which looks a bit different. Wrapbootstrap website offers really good themes for a very good price and we have found this theme: https://wrapbootstrap.com/theme/pixma-responsive-multipurpose-template-WB0B348C6. When we bought it, it was new and almost for free. It was a very good decision. We have realized how easy you can create a very nice web interface without big effort.
**jQuery** (http://jquery.com/)
  jQuery is a fast, small, and feature-rich JavaScript library. We had to use it, because jQuery is dependency for Twitter Bootstrap. We have also used it for making AJAX requests.

Authentication
--------------
**Python Social Auth** (https://github.com/omab/django-social-auth)
  Python Social Auth aims to be an easy to setup social authentication and authorization mechanism for Python projects supporting protocols like OAuth (1 and 2), OpenId and others. At the moment our site supports two OAuth2 providers: Facebook and Google+, but Python Social Auth supports more than 20 different OAuth2 providers. That's why we can easily add other providers.
**Facebook and Google+** (https://www.facebook.com/ and https://plus.google.com/)
  Facebook and Google+ are the biggest social networks. A lot of users over the world uses their services and have their accounts. Also APIs are very good documented and very easy to use.

Map
----
**Google Maps API**
**jQuery GeoComplete**

Database
--------
**PostgreSQL**
**sqlite**

Version control
---------------
**Github**

Documentation
-------------
**Read the docs**
**sphynx engine**

Deployment
----------
**Heroku**
