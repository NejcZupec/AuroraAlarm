
Discussion and Evaluation
=========================

In this chapter we would like to present and describe what have we done so far in this project. For starting point we will use the goals/instructions
for this project, provided by professor: https://sites.google.com/a/ltu.se/m7011e-2013/assignment. At the end we will check
what works and what doesn't.

Components
----------
**Backend (server-part) that stores data persistently and efficiently.**
  Backend is made with Django which uses ORM. It is persistent and efficient. At the moment we use SQL-type database, because we believe that meets the requirements of traffic for this kind of projects.
**A clearly defined and documented API for communication with the backend.**
  For API we have used Djano REST Framework. You can find it here: http://aurora-alarm.herokuapp.com/api/, documentation is accessible in API documentation chapter.
**Easy to use frontend that allows for upload of data via the web and allows the user to see all data stored in an efficient and "nice" way.**
  Our frontend tends to be simple as possible. All forms are AJAX supported and for feedback (when action is committed) a user receives a message (in green, yellow or red color). There is no save buttons. For location based inputs we have provided Google Maps integration and Google address location search. Images with provided locations are shown at map.
**All communication with the backend should be via the API from bullet 2.**
  All frontend requests are made with AJAX and jQuery library.
**A simplified but well documented example application that communicates with the backend to allow for new users to create new types of applications using your backend.**
  We provided this kind of information in API documentation chapter.
**Security on the "right level". It is recommended that a modern security scheme is used where users can login using alternative services like e.g. Google or FaceBook.**
  User can login via OAuth2 authentication system. At the moment we support Google+ and Facebook accounts, but we can extend system quite easy with other popular OAuth2 providers.
**You should understand how the security part works and be able to motivate why your solution is secure.**
  Authentication security is ensured with OAuth2 protocol. We just save minimal data about users (what OAuth2 protocol require). Django framework supports a lot of security mechanisms. We have implemented further mechanisms: cross-site-scripting (XSS) protection, cross site request forgery (CSRF) and SQL injection protection.
**The system should utilize modern HTML5-technologies of your choice.**
  Frontend is completely written with HTML5 code. We have used Twitter Bootstrap framework, which is natively written with HTML5 and CSS3 technologies. Also highcharts library is written in pure HTML5/JavaScript.

Deployment
----------
**The system should be deployed in the cloud and be publically available.**
  AuroraAlarm is deployed at Heroku. The application is accessible at: http://aurora-alarm.herokuapp.com/. All instructions, how to deploy the code, you can find it in installation chapter.

Bonus Parts
-----------
**User administration - add, remove, edit users.**
  User management can be done through RESTful API or Django's control panel.
**Data administration - interfacing databases, editing data via separate graphical interface.**
  CRUD operations for all objects can be done through Django's control panel. You can find it here: http://aurora-alarm.herokuapp.com/admin/

.. Image:: img/django_control_panel.png


**Statistics over usage (tip: Google Analytics)**
  TODO
**Connections to social media, e.g. FaceBook and Google+.**
  Users can authenticate with Facebook or Google+ accounts.
**Integrate "cool" other APIs**
  We haven't integrated any cool other APIs. We were searching aurora forecast API's, but we were not successful. Instead we have developed parsing function which collects data. This data is now accessible via API.
**Use your imagination - do that little extra...**
  We bought Twitter Bootstrap theme which helped us to make a nicer graphical interface. We were exploring with different new technologies (asynchronous processing with Celery, jQuery addons for location filtering, AJAX requests, photologue gallery,...)

What works and what doesn't
---------------------------
Our development roadmap is divided into three parts:

First stage:


Second stage:


Third stage (future work):


At the moment we have finished the first stage of the project. User interface is practically finished.

TODO: Add a conclusion and connect this topic with future work.
