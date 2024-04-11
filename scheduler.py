from dataclasses import dataclass, field
from typing import Any
import queue
import marshal
import os


class schedular:

    #establish queue
    q = queue.PriorityQueue()
    save = "data.txt"
    ###@dataclass(order=True)



    def addToQueue(self, task, Priority = False, shouldManageFiles = True):
        if(shouldManageFiles):
            self.Load(self.save)
        #add task to queue
        if Priority == True:
            try:
                #add task to front of queue
                self.q.put_nowait(task)
                if(shouldManageFiles):
                    self.Save(self.save)
                return "Task Added"
            except Exception as e:
                return "Error Occured", e
        elif Priority == False:
            try:
                #add task to end of queue
                self.q.put(task)
                if(shouldManageFiles):
                    self.Save(self.save)
                return "Task Added"
            except Exception as e:
                return "Error Occured", e
        
        
        



    def clearQueue(self, shouldManageFiles = True):
        try:
            #clear whole queue
            self.q.queue.clear()
            if(shouldManageFiles):
                self.Save(self.save)
            return "Cleared Queue"
        except Exception as e:
            return "Failed To Clear", e
        



    def queueSize(self, shouldManageFiles = True):
        if(shouldManageFiles):
            self.Load(self.save)
        try:
            #return number of tasks in queue
            return self.q.qsize()
        except Exception as e:
            return "Failed To Get Queue Size", e
        


    def nextTask(self, shouldManageFiles = True):
        if(shouldManageFiles):
            self.Load(self.save)
        ###Broken, removes front item
        return self.q.queue[0]




    def getAllTasks(self, shouldManageFiles = True):
        if(shouldManageFiles):
            self.Load(self.save)
        #establish list
        tasks = []
        #add each task to end of the list
        for i in range(self.queueSize(False)):
            tasks.append(self.q.queue[i])
        return tasks

    def readQueue(self, shouldManageFiles = True):
        tasks = []        
        
        for i in range(self.q.qsize()):
            tasks.append(self.q.queue[i])
        return tasks

    def finishTask(self, task, shouldManageFiles = True):
        if(shouldManageFiles):
            self.Load(self.save)
        try:
            #remove task from queue
            self.q.get(task)
            self.q.task_done(task)
            if(shouldManageFiles):
                self.Save(self.save)
            return "Task Finished"
        except Exception as e:
            return "Failed To Finish Task", e
    
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

    