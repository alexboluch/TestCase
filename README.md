# Get user repositories from GIT
## For what?
We can get the names of repositories and descriptions
## How is it done?
Only lowercase logins are submitted to the form input.

When submitting to the user login form, a request is made to the database (mongodb). 
If there is no data, a REST request is sent to the github. 
The received data is processed and a new instance of the user and the repositories associated with it are created.
When the data is created, a request is sent to the QraphQL to get the data from the database. 
A bit difficult, but it should be so.
After that, the data is sent as a response to the user.

If after the user's request the login was found in the database. 
Through a query to the QraphQL, the data is displayed to the user.
## What is it made of?
Language - Python.

Framework - Django.

GraphQL - for requests(endpoint).

Database - MongoDB.










