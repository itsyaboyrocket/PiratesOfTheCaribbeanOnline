from pirates.piratesgui import InventoryPage

class ClothingPage(InventoryPage.InventoryPage):
    
    def __init__(self):
        InventoryPage.InventoryPage.__init__(self)
        self.initialiseoptions(ClothingPage)


