
class WeaponBaseAI():
    def requestTargetedSkill(todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7):
        #requestTargetedSkill(SkillId, SkillId, uint8, DoId, DoIdList, uint32, Pos, uint8) clsend airecv;  // field 876
        return

    def useTargetedSkill(todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8, todo9, todo10, todo11):
        #useTargetedSkill(SkillId, SkillId, uint8, DoId, DoIdList, SkillEffects, SkillEffects, SkillEffectsList, uint16 [], uint32, Pos, uint8) broadcast;  // field 877
        return

    def requestShipSkill(todo0, todo1, todo2, todo3, todo4):
        #requestShipSkill(SkillId, SkillId, uint8, DoId, uint32) clsend airecv;  // field 878
        return

    def useShipSkill(todo0, todo1, todo2, todo3, todo4, todo5, todo6):
        #useShipSkill(SkillId, SkillId, uint8, DoId, SkillEffects, ShipEffects, uint32) broadcast;  // field 879
        return

    def requestProjectileSkill(todo0, todo1, todo2, todo3, todo4):
        #requestProjectileSkill(SkillId, SkillId, PosHpr, uint32, uint8) clsend airecv;  // field 880
        return

    def useProjectileSkill(todo0, todo1, todo2, todo3, todo4):
        #useProjectileSkill(SkillId, SkillId, PosHpr, uint32, uint8) broadcast;  // field 881
        return

    def suggestProjectileSkillResult(todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8):
        #suggestProjectileSkillResult(SkillId, SkillId, uint8, DoId, DoIdList, Pos, Normal, uint8 [], uint32) clsend airecv;  // field 882
        return

    def setProjectileSkillResult(todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8, todo9, todo10, todo11, todo12):
        #setProjectileSkillResult(SkillId, SkillId, uint8, DoId, DoIdList, SkillEffects, SkillEffects, SkillEffectsList, Pos, Normal, uint8 [], DoId, uint32) broadcast;  // field 883
        return
