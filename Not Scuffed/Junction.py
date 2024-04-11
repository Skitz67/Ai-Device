import time
import STM
import scheduler as sch

command = input("Input command: ") #Replace with ai output command
schedular = sch.schedular()
#set class 
class app:
    #apps, function within apps
    callSigns = []
    callBack = None

    #run function from app
    def run(self, args=[]):
        print(args)
        if args == [] or args == ['']:
            print("No Variable callback")
            self.callBack()
            
        else:
            print("Variable callback")
            self.callBack(*args)

    def assignCallback(self, callBack):
        self.callBack = callBack
        return self

    #instanciate application
    def __init__ (self, signs, Callback):
        #set app names and function names for instance
        self.callSigns = signs
        self.callBack = Callback



#list of applications (basically imports)
apps = []
#full list of functions from apps
apps.append(app(["STMQ"], STM.Query).assignCallback(STM.Query))
apps.append(app(["STMS"], STM.Search))
apps.append(app(["STMD"], STM.Delete))
apps.append(app(["schAdd"], schedular.addToQueue).assignCallback(schedular.addToQueue))
apps.append(app(["schClear"], schedular.clearQueue))
apps.append(app(["schGetSize"], schedular.queueSize).assignCallback(schedular.queueSize))
apps.append(app(["schNextTask"], schedular.nextTask))
apps.append(app(["schAllTasks"], schedular.getAllTasks))
apps.append(app(["schFinishTask"], schedular.finishTask))

def imports(appname, arguements = []):

    for i in range(len(apps)):
    #get the current app for itteration
        currentApp = apps[i]

        #check if command is within the call signs of current app
        if appname in currentApp.callSigns:
            if arguements == [] or arguements == ['']:
                return currentApp.run()
            else:
                print(arguements)
                return currentApp.run(arguements)
            
        
#while True:
    #print(imports(input("AppName: "), list(input("list of args: ").split(" "))))
imports("schAdd", ["hello"])

print(imports("schGetSize"))