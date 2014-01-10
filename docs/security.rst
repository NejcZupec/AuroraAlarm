
Security
========

In this chapter we describe all security mechanisms we included in AuroraAlarm application. Our application is protected
against classical threats, such as cross-site scripting (XSS), SQL injections and cross-site request forgeries (CSRF).

Authentication and Authorization
--------------------------------
For authentication and authorization we use OAuth2 protocol, which implements high security standards. We didn't implement
this service on our own, but we have used implementation developed and tested by community. In our database we save
minimal information about users. All important data is stored at OAuth2 providers.

Cross site scripting (XSS) protection
-------------------------------------
XSS attacks allow a user to inject client side scripts into the browsers of other users. Against these attacks Django
has very good protection. We have used escape filters and default forms.

Cross-site request forgery (CSRF) protection
--------------------------------------------
CSRF attacks allow a malicious user to execute actions using the credentials of another user without that user’s knowledge
or consent. Django has built-in protection against most types of CSRF attacks, providing you have enabled and used it
where appropriate. To prevent CSRF attacks, we check for a nonce in each POST request.

SQL injection protection
------------------------
SQL injection is a type of attack where a malicious user is able to execute arbitrary SQL code on a database. This can
result in records being deleted or data leakage. By using Django’s querysets, the resulting SQL will be properly escaped
by the underlying database driver.