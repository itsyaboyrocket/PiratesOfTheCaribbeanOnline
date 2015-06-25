from pirates.movement.DistributedMovingObjectAI import DistributedMovingObjectAI

class DistributedSimpleShipAI(DistributedMovingObjectAI):
    def setParentingRules(todo0, todo1):
        #setParentingRules(string, string) broadcast ram;  // field 670
        return

    def setUniqueId(todo0):
        #setUniqueId(string) required broadcast ram;  // field 672
        return

    def setGameState(todo0, todo1, todo2):
        #setGameState(string, uint32, int16) required broadcast ram ownrecv;  // field 673
        return

    def setShipClass(todo0):
        #setShipClass(uint8) required broadcast ram db ownrecv;  // field 674
        return

    def setStyleOverride(todo0):
        #setStyleOverride(int16) required broadcast ram;  // field 675
        return

    def setLogoOverride(todo0):
        #setLogoOverride(int16) required broadcast ram;  // field 676
        return

    def setLevel(todo0):
        #setLevel(uint16) required broadcast ram;  // field 677
        return

    def setName(todo0):
        #setName(string) required broadcast ram db ownrecv;  // field 678
        return

    def setArmorStates(todo0, todo1, todo2):
        #setArmorStates(uint16/100, uint16/100, uint16/100) required db broadcast ram ownrecv;  // field 679
        return

    def setMastStates(todo0, todo1, todo2, todo3, todo4):
        #setMastStates(uint16/100, uint16/100, uint16/100, uint16/100, uint16/100) required broadcast db ram ownrecv;  // field 680
        return

    def setHealthState(todo0):
        #setHealthState(uint16/100) required broadcast ram db ownrecv;  // field 681
        return

    def setCrew(todo0):
        #setCrew(uint32 []) required broadcast ram ownrecv;  // field 682
        return

    def setBandId(todo0, todo1):
        #setBandId(uint32, uint32) broadcast ram;  // field 683
        return

    def setOwnerId(todo0):
        #setOwnerId(uint32) required broadcast ram db ownrecv;  // field 684
        return

    def setCannons(todo0, todo1):
        #setCannons(uint32 [], uint32) broadcast ram;  // field 685
        return

    def setSkillEffects(todo0):
        #setSkillEffects(BuffList) broadcast ram;  // field 686
        return

    def setIsBoardable(todo0):
        #setIsBoardable(uint8) required broadcast ram;  // field 687
        return

    def setIsExitable(todo0):
        #setIsExitable(uint8) required broadcast ram;  // field 688
        return

    def setIsFlagship(todo0):
        #setIsFlagship(int8) required broadcast ram ownrecv;  // field 689
        return

    def setSinkTimer(todo0, todo1):
        #setSinkTimer(int16, int16) broadcast ram;  // field 690
        return

    def damage(todo0, todo1, todo2, todo3):
        #damage(int16, Pos, DoId, uint16 []) broadcast;  // field 691
        return

    def setBoardableShipId(todo0):
        #setBoardableShipId(uint32) broadcast ram;  // field 692
        return

    def setIsInBoardingPosition(todo0):
        #setIsInBoardingPosition(uint8) required broadcast ram;  // field 693
        return

    def requestBoard(todo0):
        #requestBoard(uint32) airecv clsend;  // field 694
        return

    def setMovie(todo0, todo1, todo2, todo3, todo4):
        #setMovie(uint8, uint32, uint32, bool, int16) broadcast;  // field 695
        return

    def shipBoarded(todo0):
        #shipBoarded() clsend airecv;  // field 696
        return

    def leave(todo0):
        #leave(uint32) airecv clsend;  // field 697
        return

    def setDeploy(todo0, todo1):
        #setDeploy(uint8, int16) broadcast ram;  // field 698
        return

    def requestBoardFlagship(todo0):
        #requestBoardFlagship(uint32) clsend airecv;  // field 699
        return

    def boardShip(todo0):
        #boardShip(uint8) broadcast;  // field 700
        return

    def swingToShip(todo0):
        #swingToShip(uint8) broadcast;  // field 701
        return

    def setWishName(todo0):
        #setWishName(string) required db ownrecv;  // field 702
        return

    def setWishNameState(todo0):
        #setWishNameState(string) required db ownrecv;  // field 703
        return

    def setCargo(todo0):
        #setCargo(uint8 []) required broadcast ram ownrecv;  // field 704
        return

    def notifyReceivedLoot(todo0):
        #notifyReceivedLoot(uint8 []) broadcast;  // field 705
        return

    def setCaptainId(todo0):
        #setCaptainId(DoId) broadcast ram;  // field 706
        return

    def setBadge(todo0, todo1):
        #setBadge(int8, int8) required broadcast ram;  // field 707
        return

    def setRespectDeployBarriers(todo0, todo1):
        #setRespectDeployBarriers(bool, uint32) broadcast ram;  // field 708
        return

    def setGuildId(todo0):
        #setGuildId(uint32) broadcast ram;  // field 709
        return

    def setClientController(todo0):
        #setClientController(uint32) broadcast ram;  // field 710
        return

    def sendCrewToIsland(todo0, todo1):
        #sendCrewToIsland(uint32, PosH);  // field 711
        return

    def dropAnchor(todo0):
        #dropAnchor(uint32) airecv clsend;  // field 712
        return

    def requestSkillEvent(todo0, todo1):
        #requestSkillEvent(uint32, uint32) airecv clsend;  // field 713
        return

    def recordSkillEvent(todo0, todo1):
        #recordSkillEvent(uint32, uint32) broadcast;  // field 714
        return

    def sendShipDefeated(todo0):
        #sendShipDefeated() broadcast;  // field 715
        return

    def setLandedGrapples(todo0):
        #setLandedGrapples(LandedGrappleList) broadcast ram;  // field 716
        return

    def setRespawnLocation(todo0, todo1):
        #setRespawnLocation(uint32, uint32);  // field 717
        return

    def setRepairCount(todo0):
        #setRepairCount(uint8) broadcast ram;  // field 718
        return

    def requestClientAggro(todo0):
        #requestClientAggro() airecv clsend;  // field 720
        return

    def requestShipRam(todo0, todo1, todo2):
        #requestShipRam(DoId, Pos, uint32) clsend airecv;  // field 721
        return

    def useShipRam(todo0):
        #useShipRam(Pos) broadcast;  // field 722
        return

    def relayTeleportInfo(todo0):
        #relayTeleportInfo() airecv;  // field 723
        return

    def sendTeleportInfo(todo0, todo1):
        #sendTeleportInfo(uint32, uint32) ownrecv;  // field 724
        return

    def teleportAvatarAboard(todo0):
        #teleportAvatarAboard(DoId) airecv;  // field 725
        return
