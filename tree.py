from Node import *
from Edge import *
from Game import *

class Tree:
    def __init__(self, gameList):
        self.gameList = gameList 
        self.Nodes = dict()
        self.EdgeList = []

    def getGameList(self):
        return self.gameList

    def lookForNode(self, nodeNmr):
        return self.Nodes.get(nodeNmr, None)
    
    def getNode(self, nodeNmr):
        if self.lookForNode(nodeNmr):
            return self.Nodes[nodeNmr]
        else:
            print("No node of that nodeNmr")
            return None

    def newNode(self, nodeNmr, playerColor):
        node = Node(nodeNmr, playerColor)
        self.Nodes[nodeNmr] = node
        return node
    
    def addNodes(self, listOfNodes): 
        for i in range(0, len(listOfNodes)):
            currentNodeNmr = listOfNodes[i].getNodeNmr()
            playerColor = getPlayerColor(currentNodeNmr)
            self.newNode(currentNodeNmr, playerColor)

    def getNodes(self):
        return self.Nodes  

    def getTreeLength(self):
        return len(self.Nodes)
    
    def getEdgeList(self):
        return self.EdgeList

    def newEdge(self, currentNode, targetNode, weight):
        edge = Edge(currentNode, targetNode, weight)
        self.EdgeList.append(edge)
    
    def addEdgeToList(self, edge):
        edge = Edge(edge.getCurrentNode(), edge.getTargetNode(), edge.getWeight())
        self.EdgeList.append(edge)
        return edge
    
    def addEdges(self, listOfEdges):
        for i in range(0, len(listOfEdges)):
            currentEdge = listOfEdges[i]
            currentSourceNode = currentEdge.getCurrentNode()
            currentTargetNode = currentEdge.getTargetNode()
            currentWeight = currentEdge.getWeight()
            self.newEdge(currentSourceNode, currentTargetNode, currentWeight)

    def exportTree(self, fileName):
        outputFile = open(fileName, "w")
        self.printTree(outputFile)
        outputFile.close()
    
    def printTree(self, outputFile):
        for key in self.Nodes:
            self.printNode(self.Nodes[key], outputFile)
        for i in self.EdgeList:
            self.printEdge(i, outputFile)

    def printNode(self, node, outputFile):
        text = "" + str(node.getNodeNmr()) + "\n"
        outputFile.write(text)
    
    def printEdge(self, edge, outputFile):
        currentNode = edge.getCurrentNode()
        targetNode = edge.getTargetNode()
        weight = edge.getWeight()
        outputFile.write("\tedge ")
        outputFile.write(str(currentNode.getNodeNmr()))
        outputFile.write(" ")
        outputFile.write(str(targetNode.getNodeNmr()))
        outputFile.write(" ")
        outputFile.write(str(weight))
        outputFile.write("\n")
    
    def traverse(self):
        for i in range(len(self.EdgeList)):
            print("Node: ", self.Nodes[i], " Edge: ", self.EdgeList[i].getWeight())
        print("Node: ", self.Nodes[i+1], " Result: ", self.Nodes[i+1].getMetaData())
    
        '''for key in self.Edges:
            print(key, self.Edges[key])
        print("Amount of edges: ", len(self.Edges))'''
        '''print("Nodes: ")
        for i in range(len(self.Nodes)):
            print(self.Nodes[i])'''
        
    def createRoot(self):
        nodeNmr = 0
        playerColor = getPlayerColor(nodeNmr)
        rootNode = self.newNode(nodeNmr, playerColor)
        metaData = rootNode.resultsForFirstNode(self.gameList, playerColor)
        rootNode.setMetaData(metaData)
        return rootNode
    
    def createLeaf(self, game, nodeNmr): 
        playerColor = getPlayerColor(nodeNmr)
        leafNode = self.newNode(nodeNmr, playerColor)
        metaData = game.getResult()
        leafNode.setMetaData(metaData)
        self.Nodes[nodeNmr] = leafNode
    
    def lookForEdgeInNode(self, edge, node):
        edges = node.getEdges()
        for element in edges:
            if element.getCurrentNode() == edge.getCurrentNode():
                return True
        return False
    
    def lookForEdgeInList(self, edge): # Blir aldri True tydeligvis
        edges = self.getEdgeList()
        for element in edges:
            if element.getCurrentNode() == edge.getCurrentNode():
                return True
        return False       
    
    def controlNodeAndEdge(self, move, nodeNmr, node):
        targetNode = Node(nodeNmr+1, getPlayerColor(nodeNmr+1))
        edge = Edge(node, targetNode, move)
        if self.lookForNode(nodeNmr):
            if self.lookForEdgeInNode(edge, self.getNode(nodeNmr)):
                node,nodeNmr = self.goToNextNode(node,nodeNmr)
            else:
                self.addEdgeToNode(edge, node)
                self.addEdgeToList(edge)
                '''if self.lookForEdgeInList(edge) == False:
                    self.addEdgeToList(edge)'''
                node,nodeNmr = self.goToNextNode(node,nodeNmr)                    
        else:
            node = self.newNode(nodeNmr, getPlayerColor(nodeNmr))
            self.addEdgeToNode(edge, node)
            self.addEdgeToList(edge)
            '''if self.lookForEdgeInList(edge) == False:
                self.addEdgeToList(edge)'''
            node,nodeNmr = self.goToNextNode(node,nodeNmr)
        return node,nodeNmr

    def goToNextNode(self, node, nodeNmr):
        targetNode = Node(nodeNmr+1, getPlayerColor(nodeNmr+1))
        node = targetNode
        nodeNmr += 1
        return node,nodeNmr
    
    def addEdgeToNode(self, edge, node):
        edgesForNode = node.getEdges()
        edgesForNode.append(edge)
        node.setEdges(edgesForNode)

    def buildTree(self, gameList): 
        rootNode = self.createRoot()
        for game in gameList:
            targetNode = None
            moves = game.getMoves()
            node = rootNode 
            for count,move in enumerate(moves):
                if (count+1) == len(moves):
                    self.createLeaf(game, nodeNmr)
                    break
                if targetNode == None:
                    nodeNmr = node.getNodeNmr() 
                    node,nodeNmr = self.controlNodeAndEdge(move, nodeNmr, node)
                    targetNode = Node(nodeNmr+1, getPlayerColor(nodeNmr+1))
                else:
                    node,nodeNmr = self.controlNodeAndEdge(move, nodeNmr, node)
                    targetNode = Node(nodeNmr+1, getPlayerColor(nodeNmr+1))

            node = rootNode

    def NodesAndEdgesToLists(self):
        nodeList = []
        edgeList = []
        self.buildTree(self.gameList)
        nodes1 = self.getNodes()
        edges1 = self.getEdgeList()
        
        for key in nodes1:
            nodeList.append(key)

        for edge in edges1:
            list3 = []
            list3.append(edge.getCurrentNode().getNodeNmr())
            list3.append(edge.getTargetNode().getNodeNmr())
            list3.append(edge.getWeight())
            edgeList.append(list3)
        return nodeList, edgeList
            
def getPlayerColor(nodeNmr):
    playerColor = ["White", "Black"]
    if (nodeNmr%2==0): 
        return playerColor[0]
    else:
        return playerColor[1]
    


  
