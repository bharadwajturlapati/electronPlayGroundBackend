__author__ = 'bharadwaj'

# delegate to al the methods and classes from here.
import dummyClass


class delegator(object):
    #def __init__(self):
        #self.project = project
    def delegateAndCall(self,className,methodName):
        classInstance = className()
        classInstance.methodName()