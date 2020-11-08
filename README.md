## Flask application to view the hierarchy of users based on roles

### Overview of my Objects and Relations

![](https://github.com/vijaykothareddy/Data-Engineering/blob/master/Images/RBAC.png)

**classes.py** is where class objects defined for the application

*User* class is instantiated to create a user and it returns user id.

*Role* class is instantiated to assign a particular role and returns role id.

*RBAC* class is instantiated to create roles and users by the above class objects and holds user and role details

**run.py** is kind of a main program gets invoked by application

**application.py** web application routes are defined

## Let see how it works

### Prerequisites

1. Python3
2. Git
3. Virtualenv
4. Ubuntu or any linux flavour

### app_config.sh

If you have a machine with above prerequisites, running the *app_config.sh* will clone the code from this repo and set up flask.

Post completion of the script, just need run the command specified by script.

### Application directory structure

All application file are rendered into a structure as below,




### sample application UI

## SQL

Average salary of content creating lead

```SQL
select avg(salary) AVG_CONTENT_CREATOR_SALARY from employee
where roleId = (select id from roles where name ='Content Creating Lead')	

```
Hierarchy of a person with role name

```SQL
select r.name UserRole ,e.name EmployeeName
from employee e inner join roles r
on e.roleId = r.id	

```




