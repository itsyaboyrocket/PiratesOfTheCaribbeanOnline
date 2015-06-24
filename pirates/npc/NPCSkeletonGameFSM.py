from pirates.pirate import BattleNPCGameFSM

class NPCSkeletonGameFSM(BattleNPCGameFSM.BattleNPCGameFSM):
    
    def __init__(self, av):
        BattleNPCGameFSM.BattleNPCGameFSM.__init__(self, av)

    
    def cleanup(self):
        BattleNPCGameFSM.BattleNPCGameFSM.cleanup(self)


