# 1. Imported Modules
#--------------------
import numpy as np
from Game import Game
from Reader import *

def IsStockWhite(game):
    if game.getWhitePieces() == "Stockfish 15 64-bit":
        return True
    else:
        return False

def CountStockWins(gameList):
    counts = [0, 0, 0]
    for game in gameList:
        if IsStockWhite(game) and game.getResult()=="1-0" or not IsStockWhite(game) and game.getResult()=="0-1":
            counts[0] += 1
        elif IsStockWhite(game) and game.getResult()=="0-1" or not IsStockWhite(game) and game.getResult()=="1-0":
            counts[2] += 1
        else:
            counts[1] += 1
    return counts

def CountStockResults(gameList, pieces):
    whiteResults = [0, 0, 0]
    blackResults = [0, 0, 0]
    for game in gameList:
        if IsStockWhite(game):
            if game.getResult()=="1-0":
                whiteResults[0] += 1
            elif game.getResult()=="0-1":
                whiteResults[2] += 1
            else:
                whiteResults[1] += 1
        else:
            if game.getResult()=="0-1":
                blackResults[0] += 1
            elif game.getResult()=="1-0":
                blackResults[2] += 1
            else:
                blackResults[1] += 1

    if pieces=="White":
        return whiteResults
    elif pieces=="Black":
        return blackResults
    else:
        print("Wrong input")
        return None
    
def GameLenghts(gameList):
    lenghts = []
    for game in gameList:
        lenghts.append(len(game.getMoves())/2)
    return lenghts

def getStandardDeviationMoves(gameList): 
    return np.std(GameLenghts(gameList))

def getMeanMoves(gameList): #The function returns the wrong mean, in reality it's half of it. We therefore divide it in half
    return (sum(GameLenghts(gameList))/len(GameLenghts(gameList)))

def GameLenghtsWhite(gameList):
    lengths = []
    for game in gameList:
        if IsStockWhite(game):
            lengths.append(len(game.getMoves())/2)
    return lengths

def GameLenghtsBlack(gameList):
    lengths = []
    for game in gameList:
        if not IsStockWhite(game):
            lengths.append(len(game.getMoves())/2)
    return lengths

def getStandardDeviationWhiteBlack(gameList): 
    whiteSTD = np.std(GameLenghtsWhite(gameList))
    blackSTD = np.std(GameLenghtsBlack(gameList))
    return [whiteSTD, blackSTD]

def getMeanMoveWhiteBlack(gameList): #The function returns the wrong mean, in reality it's half of it. We therefore divide it in half
    whiteMean = (sum(GameLenghtsWhite(gameList))/len(GameLenghtsWhite(gameList)))
    blackMean = (sum(GameLenghtsBlack(gameList))/len(GameLenghtsBlack(gameList)))
    return [whiteMean, blackMean]


def GameLengthsStockfishWin(gameList):
    lengths = []
    for game in gameList:
        if (IsStockWhite(game) and game.getResult()=="1-0") or (not IsStockWhite(game) and game.getResult()=="0-1"):
            lengths.append(len(game.getMoves())/2)
    return lengths

def GameLenghtsStockfishLoss(gameList):
    lengths = []
    for game in gameList:
        if (IsStockWhite(game) and game.getResult()=="0-1") or (not IsStockWhite(game) and game.getResult()=="1-0"):
            lengths.append(len(game.getMoves())/2)
    return lengths

def getStandardDeviationWinLoss(gameList): 
    winSTD = np.std(GameLengthsStockfishWin(gameList))
    lossSTD = np.std(GameLenghtsStockfishLoss(gameList))
    return [winSTD, lossSTD]

def getMeanMoveWinLoss(gameList): #The function returns the wrong mean, in reality it's half of it. We therefore divide it in half
    winMean = (sum(GameLengthsStockfishWin(gameList))/len(GameLengthsStockfishWin(gameList)))
    lossMean = (sum(GameLenghtsStockfishLoss(gameList))/len(GameLenghtsStockfishLoss(gameList)))
    return [winMean, lossMean]
