from pirates.inventory import InventoryUIContainer


class InventoryUISlotContainer(InventoryUIContainer.InventoryUIContainer):
    ReferenceSlots = True
    
    def __init__(self, manager, sizeX = 1.0, sizeZ = 1.0, countX = None, countZ = None, slotList = []):
        self.slotCount = 0
        InventoryUIContainer.InventoryUIContainer.__init__(self, manager, sizeX, sizeZ, countX, countZ, slotList)

    
    def manageCells(self, slotList):
        self.slotList = slotList
        for index in range(len(self.slotList)):
            slot = self.slotList[index]
            cell = self.cellList[index]
            self.manager.assignCellSlot(cell, self.slotList[self.slotCount])
            self.slotCount += 1
        


