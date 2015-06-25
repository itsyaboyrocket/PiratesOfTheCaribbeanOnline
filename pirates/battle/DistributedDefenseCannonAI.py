from pirates.battle.DistributedIslandCannonAI import DistributedIslandCannonAI

class DistributedDefenseCannonAI(DistributedIslandCannonAI):
    def recordFireEvent(todo0):
        #recordFireEvent() airecv clsend;  // field 1430
        return

    def currentCannonType(todo0):
        #currentCannonType(uint8(0-1)) broadcast ram;  // field 1431
        return

    def addProximityAmmo(todo0, todo1, todo2, todo3):
        #addProximityAmmo(uint32, SkillId, Pos, uint32) clsend airecv;  // field 1432
        return

    def removeProximityAmmo(todo0, todo1):
        #removeProximityAmmo(uint32, bool) clsend airecv;  // field 1433
        return

    def setRemovedProximityAmmo(todo0, todo1):
        #setRemovedProximityAmmo(uint32, bool) broadcast ram;  // field 1434
        return

    def requestProximityAmmo(todo0):
        #requestProximityAmmo(uint32) clsend airecv;  // field 1435
        return

    def setProximityAmmo(todo0):
        #setProximityAmmo(AmmoInfo []) required broadcast ram;  // field 1436
        return

    def requestShotNum(todo0):
        #requestShotNum(uint32) clsend airecv;  // field 1437
        return

    def setShotNum(todo0):
        #setShotNum(uint32) required broadcast ram;  // field 1438
        return

    def requestUpgradeToRepeater(todo0):
        #requestUpgradeToRepeater() airecv clsend;  // field 1439
        return
