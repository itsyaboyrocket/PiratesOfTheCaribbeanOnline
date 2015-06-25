from pirates.battle.WeaponBaseAI import WeaponBaseAI
from pirates.distributed.DistributedInteractiveAI import DistributedInteractiveAI
from pirates.distributed.DistributedTargetableObjectAI import DistributedTargetableObjectAI

class DistributedBattleableAI(WeaponBaseAI, DistributedInteractiveAI, DistributedTargetableObjectAI):
    def setCurrentTarget(todo0):
        #setCurrentTarget(uint32) broadcast ram;  // field 2062
        return
