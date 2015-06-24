from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedNode


class DistributedDailyQuestSpot(DistributedNode.DistributedNode):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedDailyQuestSpot')

    def __init__(self, cr):
        NodePath.__init__(self, 'QuestSpot')
        DistributedNode.DistributedNode.__init__(self, cr)
        print 'New Daily Quest Spot'
        base.dqs = self

    def isBattleable(self):
        return False

    def isInvisibleGhost(self):
        return False


