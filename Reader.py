# 1. Imported Modules
# -------------------
import re
from Game import *

def Reader_ReadLine(inputFile):
    line = inputFile.readline()
    if line=="":
        return None
    return line.rstrip()

def Reader_ImportChessDataBase(filePath, numGamesInFile):
    inputFile = open(filePath, "r")
    gameList = DataBase_ReadChessDataBase(inputFile, numGamesInFile)
    inputFile.close()
    return gameList

def Reader_ExportGameToFile(game, outputFile):
    outputFile = open(outputFile, "w")
    Printer_PrintGame(game, outputFile)
    outputFile.close()

def Printer_PrintGame(game, outputFile):
    outputFile.write("Game " + str() +"\n") #Should be able to write gameNumber at the start of the game
    outputFile.write("[Event: " + str(game.getEvent()) + "]\n")
    outputFile.write("[Site: " + str(game.getSite()) + "]\n")
    outputFile.write("[Date: " + str(game.getDate()) + "]\n")
    outputFile.write("[Round: " + str(game.getRound()) + "]\n")
    outputFile.write("[White: " + str(game.getWhitePieces()) + "]\n")
    outputFile.write("[Black: " + str(game.getBlackPieces()) + "]\n")
    outputFile.write("[Result: " + str(game.getResult()) + "]\n")
    outputFile.write("[ECO: " + str(game.getECO()) + "]\n")
    outputFile.write("[Opening: " + str(game.getOpening()) + "]\n")
    outputFile.write("[Variation: " + str(game.getVariation()) + "]\n")
    outputFile.write("[PlyCount: " + str(game.getPlyCount()) + "]\n")
    outputFile.write("[Black: " + str(game.getBlackPieces()) + "]\n")
    outputFile.write("[WhiteElo: " + str(game.getWhiteElo()) + "]\n")
    outputFile.write("[BlackElo: " + str(game.getBlackElo()) + "]\n")
    outputFile.write("\n" + str(game.getMoves()) + "\n")

def DataBase_ReadChessDataBase(inputFile, numGamesInFile):
    emptyGame = Game(0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    step = 1
    line = Reader_ReadLine(inputFile)
    gameList = [emptyGame]*numGamesInFile
    metaDict = dict()
    gameCount = 0
    moves = []
    while True:
        if gameCount == numGamesInFile:
            return gameList
        if step==1: # Read a game
            if line==None:
                break
            else:
                step = 2
        elif step==2: # Read meta-data
            if re.match("\[", line):
                match = re.search("\[([a-zA-Z]+)", line)
                if match:
                    key = match.group(1)
                match = re.search(r'"([^"]+)"', line)
                if match:
                    value = match.group(1)
                metaDict[key] = value
                line = Reader_ReadLine(inputFile)
            else:
                step = 3
        elif step==3: # Read moves
            line = Reader_ReadLine(inputFile)
            if line == '':
                game = emptyGame
                game = game.exportMetadataToGame(metaDict)
                game.setMoves(moves) 
                gameList[gameCount] = game
                gameCount += 1
                moves = []
                line = Reader_ReadLine(inputFile)
                step = 1
            else:
                moves = DataBase_ReadMovesInLine(moves, line)

def DataBase_ReadMovesInLine(moves, line):
    line = cleanupLine(line)
    if line=="":
        return moves
    if re.search(r"\s\d{1,}\.\s", str(line)):
        match = re.findall(r"(([Oo0](-[Oo0]){1,2}|[KQRBN]?[a-h]?[1-8]?x?[a-h][1-8](\=[QRBN])?[+#]?(\s(1-0|0-1|1\/2-1\/2))?)\s?){1,2}", line)
        if match:
            for i in range(len(match)):
                moves.append(match[i][0])
    
    # To include final line if not enumerated:
    elif not re.search(r"\s\d{1,}\.\s", str(line)):
        match = re.findall(r"(([Oo0](-[Oo0]){1,2}|[KQRBN]?[a-h]?[1-8]?x?[a-h][1-8](\=[QRBN])?[+#]?(\s(1-0|0-1|1\/2-1\/2))?)\s?){1,2}", line)
        if match:
            for i in range(len(match)):
                moves.append(match[i][0])

    # Cleanup of move list
    moves = [x.strip(' ') for x in moves]
    moves = [moves[i] for i in range(len(moves)) if (i==0) or moves[i] != moves[i-1]]
    return moves

def cleanupLine(line):
    brackets = r"\{.*?\}"
    eval = r"\[\%\beval\b.\#\d+,\d+\]"
    
    match = re.findall(brackets, line)
    match2 = re.findall(eval, line)
    
    for i in match:
        str = i
        line = line.replace(str, " ")
    
    for i in match2:
        str = i
        line = line.replace(str, " ")
    
    return line

def Printer_PrintGameFromDatabase(gameList, gameNumber):
    game = gameList[gameNumber]
    list = []
    moves = game.getMoves()
    metaData = {"Event": game.getEvent(), "Site": game.getSite(), "Date": game.getDate(), "Round": game.getRound(), "White": game.getWhitePieces(), "Black": game.getBlackPieces(), "Result": game.getResult(), "ECO": game.getECO(), "Opening": game.getOpening(), "PlyCount": game.getPlyCount(), "WhiteElo": game.getWhiteElo(), "BlackElo": game.getBlackElo()}
    list.append(metaData)
    list.append(moves)
    return list