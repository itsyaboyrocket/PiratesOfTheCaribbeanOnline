from direct.directnotify.DirectNotifyGlobal import directNotify

from pirates.uberdog.DistributedInventory import DistributedInventory


class PirateInventory(DistributedInventory):
    notify = directNotify.newCategory('Inventory')


