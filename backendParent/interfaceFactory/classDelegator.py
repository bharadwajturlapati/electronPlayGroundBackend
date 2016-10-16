__author__ = 'bharadwaj'

# delegate to al the methods and classes from here.
from dummy import dummyClass

import sys

def str_to_class(str):
    return getattr(sys.modules[__name__], str)


class delegator(object):
    #def __init__(self):
        #self.project = project
    def delegateAndCall(self,className,methodName):
        classInstance = str_to_class(className)
        print classInstance
        methodToCall = getattr(classInstance,methodName)
        #resp = methodToCall()
        resp = methodToCall()
        print resp
        return resp