from pirates.battle.WeaponBaseAI import WeaponBaseAI

class DistributedBattleAvatarAI(WeaponBaseAI):
    def setAvatarType(todo0):
        #setAvatarType(AvatarType) required broadcast ram;  // field 884
        return

    def friendsNotify(todo0, todo1):
        #friendsNotify(int32, int8) ownrecv airecv;  // field 885
        return

    def setGameState(todo0, todo1):
        #setGameState(string, int16) broadcast ram;  // field 886
        return

    def setGhostColor(todo0):
        #setGhostColor(uint8) broadcast ram;  // field 887
        return

    def setIsGhost(todo0):
        #setIsGhost(uint8) required broadcast ram;  // field 888
        return

    def setHasGhostPowers(todo0):
        #setHasGhostPowers(uint8) required broadcast ram;  // field 889
        return

    def playMotionAnim(todo0, todo1):
        #playMotionAnim(uint8, int16) broadcast ownsend airecv;  // field 890
        return

    def setAirborneState(todo0, todo1):
        #setAirborneState(bool, int16) broadcast ownsend airecv;  // field 891
        return

    def setGroundState(todo0, todo1):
        #setGroundState(uint8, int16) broadcast ownsend airecv;  // field 892
        return

    def setCurrentTarget(todo0):
        #setCurrentTarget(uint32) broadcast ram;  // field 893
        return

    def setCurrentWeapon(todo0, todo1):
        #setCurrentWeapon(uint16, uint8) required broadcast ram;  // field 894
        return

    def setCurrentAmmo(todo0):
        #setCurrentAmmo(SkillId) required broadcast ram;  // field 895
        return

    def setCurrentCharm(todo0):
        #setCurrentCharm(uint16) required broadcast ram;  // field 896
        return

    def setShipId(todo0):
        #setShipId(uint32) ownrecv required ram airecv broadcast;  // field 897
        return

    def ramKnockdown(todo0):
        #ramKnockdown() broadcast;  // field 898
        return

    def regenUpdate(todo0):
        #regenUpdate(int16) broadcast;  // field 899
        return

    def setMaxHp(todo0):
        #setMaxHp(int32) required broadcast ram;  // field 900
        return

    def setHp(todo0, todo1):
        #setHp(int32, uint8) required broadcast ram ownrecv;  // field 901
        return

    def setLuck(todo0):
        #setLuck(int16) required broadcast ram ownrecv;  // field 902
        return

    def setMaxLuck(todo0):
        #setMaxLuck(int16) required broadcast ram;  // field 903
        return

    def setMojo(todo0):
        #setMojo(int16) required broadcast ram ownrecv;  // field 904
        return

    def setMaxMojo(todo0):
        #setMaxMojo(int16) required broadcast ram;  // field 905
        return

    def setSwiftness(todo0):
        #setSwiftness(int16) required broadcast ram ownrecv;  // field 906
        return

    def setMaxSwiftness(todo0):
        #setMaxSwiftness(int16) required broadcast ram;  // field 907
        return

    def setPower(todo0):
        #setPower(int16) required broadcast ram ownrecv;  // field 908
        return

    def setMaxPower(todo0):
        #setMaxPower(int16) required broadcast ram;  // field 909
        return

    def setLuckMod(todo0):
        #setLuckMod(int16) required broadcast ram ownrecv;  // field 910
        return

    def setMojoMod(todo0):
        #setMojoMod(int16) required broadcast ram ownrecv;  // field 911
        return

    def setSwiftnessMod(todo0):
        #setSwiftnessMod(int16/10) required broadcast ram ownrecv;  // field 912
        return

    def setHasteMod(todo0):
        #setHasteMod(int16/10) required broadcast ram ownrecv;  // field 913
        return

    def setStunMod(todo0):
        #setStunMod(int16/10) required broadcast ram ownrecv;  // field 914
        return

    def setPowerMod(todo0):
        #setPowerMod(int16) required broadcast ram ownrecv;  // field 915
        return

    def setCombo(todo0, todo1, todo2, todo3):
        #setCombo(uint8, uint8, int16, uint32) required broadcast ram;  // field 916
        return

    def setSkillEffects(todo0):
        #setSkillEffects(BuffList) required broadcast ram ownrecv;  // field 917
        return

    def setEnsnaredTargetId(todo0):
        #setEnsnaredTargetId(uint32) required broadcast ram;  // field 918
        return

    def interrupted(todo0):
        #interrupted(uint8) airecv clsend;  // field 919
        return

    def setLevel(todo0):
        #setLevel(uint16) required broadcast ram ownrecv;  // field 920
        return

    def battleRandomSync(todo0):
        #battleRandomSync();  // field 921
        return

    def setVisZone(todo0):
        #setVisZone(string) broadcast ram ownsend;  // field 922
        return

    def setInInvasion(todo0):
        #setInInvasion(bool) required broadcast ram;  // field 923
        return

    def setArmorScale(todo0):
        #setArmorScale(int16/10) broadcast ram;  // field 924
        return

    def setEmote(todo0):
        #setEmote(int32) broadcast ram airecv ownsend;  // field 925
        return

    def playEmote(todo0):
        #playEmote(int32) broadcast;  // field 926
        return
