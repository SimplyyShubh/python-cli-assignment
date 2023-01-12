
import sys
import RBAC 
from pathlib import Path

commands = RBAC.RBAC()


# print(sys.argv)
# exit(0)

def command(arguments):
    commandName = arguments[0]
    
    if commandName == "addAccess":
        commands.addAccess(arguments[1])
        commands.showAccess()
        
    elif commandName == "addResource":
        commands.addResource(arguments[1])
        commands.showResources()
        
    elif commandName == "addAccessOnResource":
        commands.addAccessOnResource(arguments[1],arguments[2])
        
    elif commandName == "addRole":
        commands.addRole(arguments[1])
        
    elif commandName == "addAccessOnResourceToRole":
        commands.addAccessOnResourceToRole(arguments[1],arguments[2],arguments[3])
        
    elif commandName == "addUser":
        commands.addUser(arguments[1])
        
    elif commandName == "addRoleToUser":
        commands.addRoleToUser(arguments[1],arguments[2])

if __name__ == "__main__":
    print("Enter commands with space seperated arguments: (to exist use CTRL+C)")
    while(True):
        arguments = input().split(" ") ;
        command(arguments)
        # print(arguments)
        