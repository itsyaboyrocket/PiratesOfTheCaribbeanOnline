from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject


class DistributedInventoryManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('InventoryManager')
    
    def sendRequestInventory(self):
        self.sendUpdate('requestInventory')


