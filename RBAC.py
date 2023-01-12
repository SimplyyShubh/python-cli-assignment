
class RBAC:
    
    # Universal 
    AccessList = []
    ResourceList = {}
    
    RoleList = {}    
    UsersList = {}
    
    #{"Resourse1" = ["Access1", "Access2"], "Resourse2" = {}}
    # ResourceWithAccess = {}
    
    #{"Role1" = {"resource1" = {"Access1"}}}
    
    def showAccess(self):
        print("AccessList =>", self.AccessList)
        return
    
    def showResources(self):
        print("Resources=>" , self.ResourceList)
        return

    def showUsers(self):
        print("Users=>" , self.UsersList)
        return

    def showRoles(self):
        print("Roles=> " , self.RoleList)
        return
    
    
    #main functions
    def addAccess(self,AccessName):
        self.AccessList.append(AccessName)
        return
    
    def addResource(self,ResourceName):
        if ResourceName not in self.ResourceList:
            self.ResourceList[ResourceName]= []
        
        return
        
    def addAccessOnResource(self,AccessName,ResourceName):
        #Add access to the resource in Universal resourceList
        if(ResourceName in self.ResourceList):
            if AccessName not in self.ResourceList[ResourceName]:
                self.ResourceList[ResourceName].append(AccessName)
                
        return
        
    def addRole(self,RoleName):
        if RoleName not in self.RoleList:
            self.RoleList[RoleName] = {}
            
        self.showRoles() ;
        return
    
    def addAccessOnResourceToRole(self,AccessName,ResourceName,RoleName):
        if RoleName in self.RoleList:
            if AccessName in self.AccessList and ResourceName in self.ResourceList:
                if ResourceName not in self.RoleList[RoleName]:
                    self.RoleList[RoleName][ResourceName] = []
                if AccessName not in self.RoleList[RoleName][ResourceName]:
                    self.RoleList[RoleName][ResourceName].add(AccessName)
        return True
        
    def addUser(self,UserName):
        if UserName not in self.UsersList:
            self.UsersList[UserName] = {}
            
        self.showUsers() ;
        return
    
    def addRoleToUser(self,RoleName,UserName):
        if RoleName in self.RoleList and UserName in self.UsersList:
            Roles = self.RoleList[RoleName]
            if RoleName not in self.UsersList[UserName]:
                self.UsersList[UserName].append(RoleName) ;
                
        self.showUsers() ;
        return
        
    def checkAccess(self,UserName,ResourceName,AccessName):
        if UserName in self.UsersList and ResourceName in self.ResourceList and AccessName in self.AccessList:
            for Role in self.UsersList[UserName]:
                if ResourceName in self.RoleList[Role]:
                    if AccessName in self.RoleList[Role][ResourceName]:
                        print("yes")
                        return
        print("no")
        return
    
   
        
        
