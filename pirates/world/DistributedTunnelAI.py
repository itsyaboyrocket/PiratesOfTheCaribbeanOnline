from direct.distributed.DistributedNodeAI import DistributedNodeAI

class DistributedTunnelAI(DistributedNodeAI):
    def setParentingRules(todo0, todo1):
        #setParentingRules(string, string) required broadcast ram;  // field 1490
        return

    def setUniqueId(todo0):
        #setUniqueId(string) required broadcast ram;  // field 1491
        return

    def setModelPath(todo0):
        #setModelPath(string) required broadcast ram;  // field 1492
        return

    def setLinks(todo0):
        #setLinks(TunnelLink []) required broadcast ram;  // field 1493
        return

    def requestArea(todo0):
        #requestArea(string) airecv clsend;  // field 1494
        return

    def setArea(todo0, todo1, todo2):
        #setArea(Locations, DoId, bool) airecv clsend;  // field 1495
        return

    def sendLeaveTunnelDone(todo0):
        #sendLeaveTunnelDone() airecv clsend;  // field 1496
        return
