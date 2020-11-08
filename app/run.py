from classes import RBAC
import json

# Function called from application with uid parameter to get
# sub ordinates for that user
# Roles and Users are instantiated 

def drive(uid):
    rbac = RBAC()
    role_id2 = rbac.create_role("Sys Admin", 0, 1)
    role_id3 = rbac.create_role("Loc Mgr", 1, 2)
    role_id4 = rbac.create_role("Superviser", 2, 3)
    role_id5 = rbac.create_role("Employee", 3, 4)
    role_id6 = rbac.create_role("Trainer", 3, 5)
    rbac.create_user("Adam Admin", role_id2, 1)
    rbac.create_user("Emily Employee", role_id5, 2)
    rbac.create_user("Sam Supervisor", role_id4, 3)
    rbac.create_user("Mary Manager", role_id3, 4)
    rbac.create_user("Trent Trainer", role_id6, 5)

    # json responce construction

    sub={}
    for a,b in rbac.get_user(uid).items():
        sub[a] = b.Name
    json_string = json.dumps(sub)
    return json_string
