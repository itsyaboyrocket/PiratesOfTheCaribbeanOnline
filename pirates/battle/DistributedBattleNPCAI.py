from pirates.battle.DistributedBattleAvatarAI import DistributedBattleAvatarAI

class DistributedBattleNPCAI(DistributedBattleAvatarAI):
    def setName(todo0):
        #setName(string) required broadcast ram;  // field 927
        return

    def setSpawnPos(todo0, todo1, todo2):
        #setSpawnPos(int16/10, int16/10, int16/10) required broadcast ram;  // field 928
        return

    def setAmbush(todo0):
        #setAmbush(uint8) broadcast ram;  // field 929
        return

    def ambushIntroDone(todo0):
        #ambushIntroDone() airecv clsend;  // field 930
        return

    def boardVehicle(todo0):
        #boardVehicle(uint32) broadcast ram;  // field 931
        return

    def setSpawnPosIndex(todo0):
        #setSpawnPosIndex(string) required broadcast ram;  // field 932
        return

    def setAssociatedQuests(todo0):
        #setAssociatedQuests(uint16 []) required broadcast ram;  // field 933
        return

    def setSpawnIn(todo0):
        #setSpawnIn(int32) broadcast ram;  // field 934
        return

    def setChat(todo0, todo1):
        #setChat(string, uint8) broadcast ownsend;  // field 935
        return

    def setActorAnims(todo0, todo1, todo2, todo3):
        #setActorAnims(string, string, string, string) required broadcast ram;  // field 936
        return

    def requestAnimSet(todo0):
        #requestAnimSet(string) broadcast;  // field 937
        return

    def setCollisionMode(todo0):
        #setCollisionMode(uint8) required broadcast ram;  // field 938
        return

    def setInitZ(todo0):
        #setInitZ(int16/10) required broadcast ram;  // field 939
        return

    def requestClientAggro(todo0):
        #requestClientAggro() airecv clsend;  // field 940
        return

    def setIsAlarmed(todo0, todo1):
        #setIsAlarmed(bool, int16/10) broadcast ram;  // field 941
        return

    def requestHostilize(todo0):
        #requestHostilize() airecv clsend;  // field 942
        return

    def setIsPet(todo0):
        #setIsPet(bool) required broadcast ram;  // field 943
        return
