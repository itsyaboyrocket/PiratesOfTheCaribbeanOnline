
class DistributedPlayerSimpleShipUD():
    def attacked(todo0):
        #attacked() broadcast;  // field 728
        return

    def setSiegeBounty(todo0):
        #setSiegeBounty(uint16) broadcast ram;  // field 729
        return

    def setShipUpfitList(todo0):
        #setShipUpfitList(uint8 []) required broadcast ram db ownrecv;  // field 730
        return

    def setThreatLevel(todo0):
        #setThreatLevel(int8) broadcast ram;  // field 731
        return

    def setOpenPort(todo0):
        #setOpenPort(int8) broadcast ram;  // field 732
        return

    def setAllowCrewState(todo0):
        #setAllowCrewState(bool) airecv required broadcast ram ownsend;  // field 733
        return

    def setAllowFriendState(todo0):
        #setAllowFriendState(bool) airecv required broadcast ram ownsend;  // field 734
        return

    def setAllowGuildState(todo0):
        #setAllowGuildState(bool) airecv required broadcast ram ownsend;  // field 735
        return

    def setAllowPublicState(todo0):
        #setAllowPublicState(bool) airecv required broadcast ram ownsend;  // field 736
        return

    def setBoardingChoice(todo0):
        #setBoardingChoice(uint8) ownsend airecv;  // field 737
        return

    def setWillFullyRepairShip(todo0):
        #setWillFullyRepairShip(bool) broadcast ram;  // field 738
        return

    def sunkAShipFanfare(todo0):
        #sunkAShipFanfare(DoId) broadcast;  // field 739
        return

    def clientReachedRespawnLocation(todo0):
        #clientReachedRespawnLocation() airecv clsend;  // field 740
        return
