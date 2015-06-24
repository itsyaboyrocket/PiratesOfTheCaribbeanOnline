from pirates.inventory.InventoryUIGlobals import *
from pirates.inventory import InventoryUIItem

class InventoryUINoTradeItem(InventoryUIItem.InventoryUIItem):
    
    def __init__(self, manager, itemTuple, imageScaleFactor = 1.0, showMax = 1):
        InventoryUIItem.InventoryUIItem.__init__(self, manager, itemTuple, imageScaleFactor = imageScaleFactor)
        self.initialiseoptions(InventoryUINoTradeItem)
        self['relief'] = None
        self.textScale = 0.90000000000000002
        self.itemType = ITEM_NOTRADE


