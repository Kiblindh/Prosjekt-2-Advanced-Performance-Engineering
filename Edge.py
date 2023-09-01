class Edge:
    def __init__(self, currentNode, targetNode, weight):
        self.currentNode = currentNode
        self.targetNode = targetNode
        self.weight = weight

    def getCurrentNode(self):
        return self.currentNode
    
    def setCurrentNode(self, currentNode):
        self.currentNode = currentNode

    def getTargetNode(self):
        return self.targetNode
    
    def setTargetNode(self, targetNode):
        self.targetNode = targetNode

    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        self.weight = weight
    
    def __str__(self):
        return str(self.currentNode) + "-" + str(self.targetNode) + " " + str(self.weight)