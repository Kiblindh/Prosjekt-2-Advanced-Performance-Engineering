# Chess Games
class Game:
    def __init__(self, event, site, date, round, whitePieces, blackPieces, result, ECO, opening, variation, plyCount, whiteElo, blackElo, moves):
        self.event = event
        self.site = site
        self.date = date
        self.round = round
        self.whitePieces = whitePieces
        self.blackPieces = blackPieces
        self.result = result
        self.ECO = ECO
        self.opening = opening
        self.variation = variation
        self.plyCount = plyCount
        self.whiteElo = whiteElo
        self.blackElo = blackElo
        self.moves = moves
        self.gameDict = dict()

    # -------------------Get-functions for the game class -------------

    def getEvent(self):
        return self.event
    
    def getSite(self):
        return self.site
    
    def getDate(self):
        return self.date
    
    def getRound(self):
        return self.round
    
    def getWhitePieces(self):
        return self.whitePieces
    
    def getBlackPieces(self):
        return self.blackPieces
    
    def getResult(self):
        return self.result
    
    def getECO(self):
        return self.ECO
    
    def getOpening(self):
        return self.opening
    
    def getVariation(self):
        return self.variation
    
    def getPlyCount(self):
        return self.plyCount
    
    def getWhiteElo(self):
        return self.whiteElo
    
    def getBlackElo(self):
        return self.blackElo
    
    def getMoves(self):
        return self.moves
    
    def setMoves(self, moves):
        self.moves = moves

    def getGameDict(self):
        return self.gameDict
    
    def setGameDict(self, gameDict):
        self.gameDict = gameDict
    
    def newGame(self, event, site, date, round, whitePieces, blackPieces, result, ECO, opening, variation,plyCount, whiteElo, blackElo, moves):
        game = Game(event, site, date, round, whitePieces, blackPieces, result, ECO, opening, variation, plyCount, whiteElo, blackElo, moves)
        self.gameDict[round] = game
        return game

    def getWinner(self):
        if self.getResult()=="1-0":
            return self.whitePieces
        elif self.getResult()=="0-1":
            return self.blackPieces
        else:
            print("It was a draw")
            return None
    
    def getNumMoves(self):
        return len(self.getMoves())
    
    def lookForGame(self, round):
        return self.gameDict.get(round, None)
    
    def exportMetadataToGame(self, metaDict):
        if metaDict.get("Variation", None) == None:
            metaDict["Variation"] = ""
        return self.newGame(metaDict["Event"], metaDict["Site"], metaDict["Date"], metaDict["Round"], metaDict["White"], metaDict["Black"], metaDict["Result"], metaDict["ECO"], metaDict["Opening"], metaDict["Variation"], metaDict["PlyCount"], metaDict["WhiteElo"], metaDict["BlackElo"], [])
