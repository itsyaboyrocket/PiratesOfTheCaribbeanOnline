from pandac.PandaModules import *
from direct.showbase.PythonUtil import report

from pirates.instance import DistributedInstanceBase


class DistributedPiratesTutorialWorld(DistributedInstanceBase.DistributedInstanceBase):
    notify = directNotify.newCategory('DistributedPiratesTutorialWorld')
    
    def __init__(self, cr):
        DistributedInstanceBase.DistributedInstanceBase.__init__(self, cr)
        self.tutorialHandler = None
        self.tutorialHandlerId = 0

    
    def setTutorialHandlerId(self, doId):
        self.tutorialHandlerId = doId
        
        def tutorialHandlerExists(tutorialHandler):
            self.tutorialHandler = tutorialHandler
            self.tutorialHandler.setInstance(self)

        self.cr.relatedObjectMgr.requestObjects([
            self.tutorialHandlerId], eachCallback = tutorialHandlerExists)

    
    def addWorldInterest(self, area = None):
        DistributedInstanceBase.DistributedInstanceBase.addWorldInterest(self, area)
        if area:
            area.turnOn(localAvatar)
        

    addWorldInterest = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(addWorldInterest)
    
    def removeWorldInterest(self, area = None):
        if not area and area.gridVisContext:
            area = None
        
        DistributedInstanceBase.DistributedInstanceBase.removeWorldInterest(self, area)

    removeWorldInterest = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(removeWorldInterest)
    
    def turnOff(self, cacheIslands = []):
        self._turnOffIslands(cacheIslands)
        DistributedInstanceBase.DistributedInstanceBase.turnOff(self, cacheIslands)

    turnOff = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(turnOff)
    
    def turnOn(self, av = None):
        DistributedInstanceBase.DistributedInstanceBase.turnOn(self, av)
        self._turnOnIslands()

    turnOn = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(turnOn)

