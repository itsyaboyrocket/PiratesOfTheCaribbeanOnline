from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from pandac.PandaModules import *

from pirates.piratesbase import PiratesGlobals


class ClientServicesManager(DistributedObjectGlobal):
    notify = directNotify.newCategory('ClientServicesManager')

    def performLogin(self, doneEvent):
        self.doneEvent = doneEvent
        self.sendUpdate('login', ['dev'])

    def acceptLogin(self):
        messenger.send(self.doneEvent, [{'mode': 'success'}])

    def requestAvatars(self):
        self.sendUpdate('requestAvatars')

    def setAvatars(self, avatars):
        avList = {PiratesGlobals.PiratesSubId: [PiratesGlobals.AvatarSlotAvailable,
                                                PiratesGlobals.AvatarSlotAvailable,
                                                PiratesGlobals.AvatarSlotAvailable,
                                                PiratesGlobals.AvatarSlotAvailable]}
        self.cr.handleAvatarsList(avList)

    def sendCreateAvatar(self, avDNA, index):
        self.sendUpdate('createAvatar', [avDNA.makeNetString(), index])

    def createAvatarResp(self, avId):
        messenger.send('createdNewAvatar', [avId])

    def sendChooseAvatar(self, avId):
        self.sendUpdate('chooseAvatar', [avId])

    def avatarResponse(self, avId, avDetails):
        self.cr.handleAvatarResponseMsg(avId, avDetails)