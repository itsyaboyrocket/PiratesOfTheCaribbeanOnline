from pirates.battle.WeaponBaseAI import WeaponBaseAI
from pirates.distributed.DistributedInteractiveAI import DistributedInteractiveAI

class DistributedWeaponAI(WeaponBaseAI, DistributedInteractiveAI):
    def setMovie(todo0, todo1):
        #setMovie(uint8, uint32) broadcast ram;  // field 1416
        return

    def doAIAttack(todo0, todo1, todo2, todo3, todo4, todo5, todo6):
        #doAIAttack(int32/10, int32/10, int32/10, uint32, SkillId, SkillId, int16) broadcast;  // field 1417
        return
