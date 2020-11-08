## Flask application to view the hierarchy of users based on roles

### Overview of my Objects and Relations

![](https://github.com/vijaykothareddy/Data-Engineering/blob/master/Images/RBAC.png)

**classes.py** is where class objects defined for the application

*User* class is instantiated to create a user and it returns user id.

*Role* class is instantiated to assign a particular role and returns role id.

*RBAC* class is instantiated to create roles and users by the above class objects and holds user and role details

**run.py** is kind of a main program gets invoked by application

**application.py** web application routes are defined




