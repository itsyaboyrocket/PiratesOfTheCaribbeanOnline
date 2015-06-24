from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify import DirectNotifyGlobal


class DistributedCannonDefenseEntrance(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedInteractive')
    
    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self._gameFullTxt = None
        self._gameFullSeq = None

    
    def generate(self):
        DistributedObject.generate(self)

    
    def announceGenerate(self):
        DistributedObject.announceGenerate(self)

    
    def teleport(self):
        base.loadingScreen.showTarget(cannonDefense = True)
        base.cr.loadingScreen.show()


