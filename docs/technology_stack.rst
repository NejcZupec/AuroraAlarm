
Technology Stack
================

AuroraAlarm is built with quite new and popular, open source technologies. In this project we wanted to learn and try, how to use
all these technologies and how they interact between each other. Further we would like to list all technologies we have used
and write a short description for each and why we have chosen it. Usually the main reason for technology choice was a good
documentation. We think this is the main advantage, when you have to select between different technologies.

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
**Google Maps API** (https://developers.google.com/maps/documentation/javascript)
  Google Maps is a web mapping service application and technology provided by Google. It is very simple to use, with powerful API and good documentation.

**Geocomplete** (http://ubilabs.github.io/geocomplete/)
  Geocomplete is an advanced jQuery plugin that wraps the Google Maps API's Geocoding and Places Autocomplete services. We decided for it, basically because it works naturally with jQuery and has a good documentation.

Database
--------
**PostgreSQL** (http://www.postgresql.org/)
  PostgreSQL is a powerful, open source object-relational database system. We use it in deployed version at Heroku, because this the main choice and it works good. We didn't want to complicate with NoSQL databases, because our data scheme is very simple and SQL works good enough.

**sqlite** (http://www.sqlite.org/)
  SQLite is a software library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. It is very easy to use for development purposed. It has been already installed with Django and it works very good, when you have to develop in a team.

Version control
---------------
**Github** (https://github.com/)
  GitHub is a web-based hosting service for software development projects that use the Git revision control system. We decided for it mainly because of git. It is really good tool for source control and also team work. We have really good experience with it and we recommended it!

Documentation
-------------
**Read the docs** (https://readthedocs.org/)
  Read the Docs hosts documentation, making it fully searchable and easy to find. You can import your docs using any major version control system, including Mercurial, Git, Subversion, and Bazaar. Final documentation looks really nice and integration with Github is perfect.

**Sphynx engine** (http://sphinx-doc.org/)
  Sphinx is a tool that makes it easy to create intelligent and beautiful documentation. In combination with *Read the docs* and *Github* it enables you to create documentation sites, very easy and efficient. It has a bit complicated syntax, but you know how to use it, it's very straightforward.

Deployment
----------
**Heroku** (https://www.heroku.com/)
  Heroku is a cloud platform as a service (PaaS) supporting several programming languages. We have decided for it, because we wanted to try this a very popular platform. We had some troubles, but after a couple of days we have succeeded. Maybe it would be easier to use Amazon, but at least we learned something new and see how Heroku works.
**Gunicorn** (http://gunicorn.org/)
  The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP Server for Unix.
