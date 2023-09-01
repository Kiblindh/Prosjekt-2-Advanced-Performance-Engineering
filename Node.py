class Node:
    def __init__(self, nodeNmr, playerColor):
        self.nodeNmr = nodeNmr
        self.playerColor = playerColor
        
        self.metaData = [] 
        self.edges = []

    def getNodeNmr(self):
        return self.nodeNmr
    
    def setNodeNmr(self, nodeNmr):
        self.nodeNmr = nodeNmr
    
    def getPlayerColor(self):
        return self.playerColor
    
    def setPlayerColor(self, playerColor):
        self.playerColor = playerColor

    def getEdges(self):
        return self.edges
    
    def setEdges(self, edges):
        self.edges = edges
    
    def setMetaData(self, metaData):
        self.metaData = metaData
    
    def getMetaData(self):
        return self.metaData
    
    def __str__(self): 
        return str(self.nodeNmr)
    
    def resultsForFirstNode(self, gameList, playerColor):
        # Wins, draws, losses
        whiteResults = [0, 0, 0]
        blackResults = [0, 0, 0]
        for game in gameList:
            if game.getResult()=="1-0":
                whiteResults[0] += 1
                blackResults[2] += 1
            elif game.getResult()=="0-1":
                whiteResults[2] += 1
                blackResults[0] += 1
            else:
                whiteResults[1] += 1
                blackResults[1] += 1 
        
        if playerColor=="White":
            return whiteResults
        elif playerColor=="Black":
            return blackResults
        else:
            print("Wrong input for playerColor")
            return None

    def getEdgesForNode(self, gameList):
        listOfEdges = []
        nodeNmr = self.getNodeNmr()
        for game in gameList:
            moves = game.getMoves()
            if nodeNmr == 0:
                nextMove = moves[nodeNmr]
                if nextMove not in listOfEdges:
                    listOfEdges.append(moves[nodeNmr]) 
            else:
                nextMove = moves[nodeNmr - 1]
                if nextMove not in listOfEdges:
                    listOfEdges.append(moves[nodeNmr - 1]) 

        return listOfEdges

# Task 12:
def openingWins(gameList, opening, pieces): 
    # Wins, draws, losses
    whiteResults = [0, 0, 0]
    blackResults = [0, 0, 0]
    for game in gameList:
        if game.getOpening() == opening:
            if game.getResult()=="1-0":
                whiteResults[0] += 1
                blackResults[2] += 1
            elif game.getResult()=="0-1":
                whiteResults[2] += 1
                blackResults[0] += 1
            else:
                whiteResults[1] += 1
                blackResults[1] += 1 
    
    if pieces=="White":
        return whiteResults
    elif pieces=="Black":
        return blackResults
    else:
        print("Wrong input")
        return None



