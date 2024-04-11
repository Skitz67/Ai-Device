import json 
import os
def write (data, file, removefile=False):
    try:
        with open(file, "w") as f:
         
            if removefile == True:
                os.remove(file)
                
                f = open(file, "x+")
            f.write(str(data))
            f.close()
            return "Success"
    except Exception as e:
        return "Failed",e
    
def read (file):
    try:
        f = open(file, "r")
        data= f.read()
        f.close()
        return "Success",data
    except Exception as e:
        return "Failed",e

def create(file):
    try:
        f = open(file, "x")
        return "Success"
    except Exception as e:
        return "Failed",e
