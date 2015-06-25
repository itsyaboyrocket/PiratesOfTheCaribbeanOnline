from pirates.world.DistributedGameAreaAI import DistributedGameAreaAI
from direct.distributed.DistributedCartesianGridAI import DistributedCartesianGridAI

class DistributedIslandAI(DistributedGameAreaAI, DistributedCartesianGridAI):
    def setParentingRules(todo0, todo1):
        #setParentingRules(string, string) required broadcast ram;  // field 1480
        return

    def setIslandTransform(todo0, todo1, todo2, todo3):
        #setIslandTransform(int32/10, int32/10, int32/10, int32/10) broadcast required ram;  // field 1481
        return

    def setZoneSphereSize(todo0, todo1, todo2):
        #setZoneSphereSize(uint16, uint16, uint16) required broadcast ram;  // field 1482
        return

    def setZoneSphereCenter(todo0, todo1):
        #setZoneSphereCenter(int32, int32) required broadcast ram;  // field 1483
        return

    def setIslandModel(todo0):
        #setIslandModel(string) required broadcast ram;  // field 1484
        return

    def setUndockable(todo0):
        #setUndockable(bool) required broadcast;  // field 1485
        return

    def setPortCollisionSpheres(todo0):
        #setPortCollisionSpheres(PortCollisionSphere []) required broadcast ram;  // field 1486
        return

    def makeLavaErupt(todo0):
        #makeLavaErupt() broadcast;  // field 1487
        return

    def setFeastFireEnabled(todo0):
        #setFeastFireEnabled(bool) required broadcast ram;  // field 1488
        return

    def setFireworkShowEnabled(todo0, todo1):
        #setFireworkShowEnabled(bool, uint8) required broadcast ram;  // field 1489
        return
