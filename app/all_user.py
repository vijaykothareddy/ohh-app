import json
class Role(object):
    #uid = 0
    roles = {}

    def __init__(self, name=None, parent=-1, uid=-1):
        """Initializes the a role with the permissions associated with it.
        """
        
        self.Name = name
        self.Parent = parent
        #Role.uid += 1
        self.uid = uid
        #self.id = Role.uid
        #Role.roles[name] = self

    def get_name(self):
        """returns the name of the role
        """
        return self.Name

    def get_parent(self):
        return self.Parent

    def get_id(self):
        return self.uid



class User(object):
    """A role gets assigned to a user
    """
    uid = 0


    def __init__(self, name=None, role=-1, uid=-1):
       
        self.Name = name
        #User.uid += 1
        #self.id = User.uid
        self.uid = uid
        self.role = role

    def add_role(self, role):
        self.role = role



class RBAC(object):
    def __init__(self):
        self.users = []
        self.roles = []
        self.userdetails ={}
        self.roledetails = {}

    def create_user(self, name, role, uid):
        
        user = User(name, role, uid)
        self.users.append(user)
        self.userdetails[user.uid] = user
        self.roledetails[user.role] = user
        return user.uid

    def create_role(self, name, parent, uid):
        role = Role(name, parent, uid)
        self.roles.append(role)
        return role.uid


    def get_users(self):
        return self.users

    def get_roles(self):
        return self.roles

    def get_user(self, user_id):
        #print(self.userdetails.keys())
        #print(self.roledetails.keys())
        #print(user_id)
        user = self.userdetails.get(user_id)
        role_id = user.role
        #print (dict((k, v) for k, v in self.roledetails.items() if v.role <= role_id))
        return dict((k, v) for k, v in self.roledetails.items() if k > role_id)
