from Reader import *

class OpeningManagement:
    
    def __init__(self, gameList):
        self.gameList = gameList
        self.openingCountDict = self.getOpeningCountDict()

    def getOpeningCountDict(self):
            #Gets all the openings from gameList in the constructor, and then the key becomes the opening and the value of the key is the amount of times the opening is played
            openingDict = {}
            for game in self.gameList:
                if game.getOpening() in openingDict:
                    openingDict[game.getOpening()] += 1
                else:
                    openingDict[game.getOpening()] = 1
            return openingDict

    def lookAtNOpenings(self, n): #Returns a list with the openings played more than n times
        openingsMoreNTimes = []
        for opening in self.openingCountDict:
            if(self.openingCountDict[opening] > n):
                openingsMoreNTimes.append(opening)
        return openingsMoreNTimes

    def getAmountOfDifferentOpenings(self): #Returns the amount of different openings that has been played
        keysList = list(self.openingCountDict.keys())
        return len(keysList)

    def getOpeningDict(self): #Returns an opening dictionary with key[Openings played in gameList] and value[Game objects that the games are played in]
        openingDict = dict()
        for game in self.gameList:
            opening = game.getOpening()
            if openingDict.get(opening, None)==None:
                openingDict[opening] = game
                
        openingDict = self.fillOpeningDict(openingDict)

        return openingDict
        
    def fillOpeningDict(self, openingDict):
        for key in openingDict:
            valueList = []
            for game in self.gameList:
                if game.getOpening() == key:
                    valueList.append(game)
            openingDict[key] = valueList
            
        return openingDict

    def openingWins(self, opening, pieces): #Gets the results for the chosen opening, have to choose black or white pieces in the parameter
        # Wins, draws, losses
        whiteResults = [0, 0, 0]
        blackResults = [0, 0, 0]
        for game in self.gameList:
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

    def getResultForNOpenings(self, n): #Gets the result of black and white pieces in a list (one white and one black) for the openings that's played more than n times
        #openingDict = self.getOpeningCountDict(self.gameList)
        openingDict = self.openingCountDict
        BiggerThanNOpenings = self.lookAtNOpenings(n)
        OpeningResultWhite = []
        OpeningResultBlack = []
        for i in range(0, len(BiggerThanNOpenings)):
            OpeningResultBlack.append([BiggerThanNOpenings[i], self.openingWins(BiggerThanNOpenings[i], "Black")])
            OpeningResultWhite.append([BiggerThanNOpenings[i], self.openingWins(BiggerThanNOpenings[i], "White")])
        return OpeningResultWhite, OpeningResultBlack
