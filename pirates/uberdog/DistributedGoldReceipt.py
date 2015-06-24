from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObject import DistributedObject


class DistributedGoldReceipt(DistributedObject):
    notify = directNotify.newCategory('GoldReceipt')
    
    def setGoldPaid(self, goldPaid):
        self.goldPaid = goldPaid

    
    def setExpirationDate(self, expirationDate):
        self.expirationDate = expirationDate


