from dataclasses import dataclass, field
from typing import Any
import queue
import marshal
import os


class schedular:

    #establish queue
    q = queue.PriorityQueue()
    ###@dataclass(order=True)



    def addToQueue(self, task, Priority = False):
        #add task to queue
        if Priority == True:
            try:
                #add task to front of queue
                self.q.put_nowait(task)
            except Exception as e:
                return "Error Occured", e
        elif Priority == False:
            try:
                #add task to end of queue
                self.q.put(task)
                return "Task Added"
            except Exception as e:
                return "Error Occured", e
        
        



    def clearQueue(self):
        try:
            #clear whole queue
            self.q.queue.clear()
            return "Cleared Queue"
        except Exception as e:
            return "Failed To Clear", e



    def queueSize(self):
        try:
            #return number of tasks in queue
            return self.q.qsize()
        except Exception as e:
            return "Failed To Get Queue Size", e
        


    def nextTask(self):
        ###Broken, removes front item
        return self.q.queue[0]




    def getAllTasks(self):
        #establish list
        tasks = []
        #add each task to end of the list
        for i in range(self.queueSize()):
            tasks.append(self.q.queue[i])
        return tasks



    def finishTask(self, task):
        try:
            #remove task from queue
            self.q.get(task)
            self.q.task_done(task)
            return "Task Finished"
        except Exception as e:
            return "Failed To Finish Task", e
    
    def Save(self, filename):
        f1 = open(filename, "w")
        f1.truncate(0)
        f1.write(str(self.getAllTasks()))
        f1.close()

    def Load(self, filename):
        f1 = open(filename, "r")
        data = f1.read()
        data = data.replace("[", "").replace("]", "")
        dataList = data.split(", ")
        self.clearQueue()
        for i in range(len(dataList)):
            self.addToQueue(dataList[i])


        
