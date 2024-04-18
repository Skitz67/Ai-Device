from dataclasses import dataclass, field
from typing import Any
import queue
import marshal
import os


class schedular:

    #establish queue
    q = queue.PriorityQueue()
    savefile = "data.txt"
    


    def addToQueue(self, task, Priority = "False", shouldManageFiles = "True"):
        if shouldManageFiles == "True":
            self.Load(self.savefile)
        #add task to queue

        if Priority == "True":
            datalist = self.Load(self.savefile)
            #add task to front of list
            datalist.insert(0, task)
            self.q.queue.clear()
            #adds list back into queue
            for i in range(len(datalist)):
                 self.q.put(datalist[i])

            if shouldManageFiles == "True":
                self.Save(self.savefile)

            return "Task Added"
        elif Priority == "False":
                #add task to end of queue
                self.q.put(task)
                if shouldManageFiles == "True":
                    self.Save(self.savefile)
                return "Task Added"


    def clearQueue(self, shouldManageFiles = "True"):
            #clear whole queue
            self.q.queue.clear()
            if shouldManageFiles == "True":
                self.Save(self.savefile)
            return "Cleared Queue"


    def queueSize(self, shouldManageFiles = "True"):
        if shouldManageFiles == "True":
            self.Load(self.savefile)
        #return number of tasks in queue
        return self.q.qsize()


    def nextTask(self, shouldManageFiles = "True", block = True):
        if shouldManageFiles == "True":
            self.Load(self.savefile)

        return self.q.get(block)

        



    def getAllTasks(self, shouldManageFiles = "True"):
        if shouldManageFiles == "True":
            self.Load(self.savefile)
        #establish list
        tasks = []
        #add each task to end of the list
        for i in range(self.queueSize(False)):
            tasks.append(self.q.queue[i])
        return tasks


    def readQueue(self, shouldManageFiles = "True"):
        tasks = []        
        
        for i in range(self.q.qsize()):
            tasks.append(self.q.queue[i])
        return tasks


    def finishFirstTask(self, shouldManageFiles = "True"):
        if shouldManageFiles == "True":
            self.Load(self.savefile)
            #remove task from queue
            self.q.task_done()
            if shouldManageFiles == "True":
                self.Save(self.savefile)
            return "Task Finished"
        else:
            self.q.task_done()
            return "Task Finished"

    
    def Save(self, filename):
        f1 = open(filename, "w")
        f1.truncate(0)
        f1.write(str(self.readQueue()))
        f1.close()


    def Load(self, filename):
        f1 = open(filename, "r")
        data = f1.read()
        data = data.replace("[", "").replace("]", "").replace("'", "").replace('"', "")
        dataList = data.split(", ")
        self.q.queue.clear()
        for i in range(len(dataList)):
            self.q.put(dataList[i])
        return dataList

    