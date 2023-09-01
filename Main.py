# Group 24 - Sipan Omar, Kim-Iver Brevik Blindheimsvik og Morten Husby Sande

# 1. Imported modules
# -------------------------------------------
from Reader import *
from Game import *
from Counter import *
from Excel import *
from Plotting import *
from tree import *
from HTMLFile import *

# 2. Global variables
# --------------------------------------------
inputFile = "Stockfish_15_64-bit.commented.[2600].pgn"
outputFile = "testFile.txt"
separator = ","
inputSheet = 'Chess.xlsx'
numberOfGamesToShow = 2600
gameList = Reader_ImportChessDataBase(inputFile, numberOfGamesToShow)
plots = Plots(gameList)

# 3. Main
# --------------------------------------------



# --------------------------------------------
# Task 1
# --------------------------------------------
'''We can test that the game class works by using the global gameList.
We've also created a __str__() method in the game class so that we can write out
a game object. Underneath you can see the information a game object contains'''
'''
game_task1 = gameList[30]
print(game_task1)
'''
# --------------------------------------------
# Task 2:
# --------------------------------------------

'''The reader_ImportFromChessDatabase(file) function allows us to read from a file
given in the format of the stockfish file. Using this function we can export all
the games from a file. For example we can choose the first element in the gameList
variable given in global elements. By printing this we can see that we've imported
a game from the file. Here it's important to remember that a list starts at index 0,
so you have to choosen gameList[0] to get game 1, and likewise gameList[2599] to get
the last game, game 2600.'''

#print(gameList[2599])

# --------------------------------------------
# Task 3:
# -------------------------------------------
'''
testGame = gameList[0] #Gets a game from the database
Reader_ExportGameToFile(testGame, outputFile, separator)  #Exports game to a text file
'''

# --------------------------------------------
# Task 5:
# --------------------------------------------

#Exporting a game to excel
'''
game1001 = Printer_PrintGameFromDatabase(gameList,1001) #takes in gameList and the game number from 0 to 2599
#print(game1001)
ExportGameExcel(game1001, inputSheet)
game1003 = Printer_PrintGameFromDatabase(gameList,1003)
#print(game1003)
ExportGameExcel(game1003, inputSheet)
'''
#Importing a game from the excel file
'''
game1 = (ImportGameExcel('823.2.8', inputSheet))
print(game1)
'''

# --------------------------------------------
# Task 6:
# --------------------------------------------

#The document is created at the end of the main file in task 12 
#The document is called document.html. 

# --------------------------------------------
# Task 7:
# --------------------------------------------
'''
whiteCounts = CountStockResults(gameList, "White")
blackCounts = CountStockResults(gameList, "Black")
print("White: W: ", whiteCounts[0], " D: ", whiteCounts[1], " L: ", whiteCounts[2])
print("Black: W: ", blackCounts[0], " D: ", blackCounts[1], " L: ", blackCounts[2])
'''
#Plotting of results
'''
plots.PlotResults('stockfishWins')
plots.PlotResults('colorWins')
'''
# --------------------------------------------
# Task 8:
# --------------------------------------------
'''
plots.PlotOngoning()
print('Mean of the number of moves of a game: ', round(getMeanMoves(gameList),1))
print('Standard deviation of the number of moves of a game: ',round((getStandardDeviationMoves(gameList)),1))

plots.PlotOngoingWhiteAndBlack()
print('Mean of the number of moves of a game played as white/black: ', round(getMeanMoveWhiteBlack(gameList)[0],1), '/', round(getMeanMoveWhiteBlack(gameList)[1],1))
print('Standard deviation of the number of moves of a game where stockfish played as white/black: ',round(getStandardDeviationWhiteBlack(gameList)[0],1),'/',round(getStandardDeviationWhiteBlack(gameList)[1],1))

plots.PlotOngoingWinAndLoss()
print('Mean of the number of moves of a game won/lost by stockfish: ', round(getMeanMoveWinLoss(gameList)[0],1), '/', round(getMeanMoveWinLoss(gameList)[1],1))
print('Standard deviation of the number of moves of a game won/lost by stockfish: ',round(getStandardDeviationWinLoss(gameList)[0],1),'/',round(getStandardDeviationWinLoss(gameList)[1],1))
'''
# --------------------------------------------
# Task 9 & 10:
# --------------------------------------------
# The data structure and management functions can be seen in the Node/tree/edge.py modules
'''
ogtree = Tree(gameList)
ogtree.buildTree(gameList)

print("Nodes:")
nodes = ogtree.getNodes()
print(len(nodes))'''

# --------------------------------------------
# Task 11:
# --------------------------------------------

#This data is presented in the HTML document

#print(Printer_PrintGameFromDatabase(gameList, 0))

#plots.plotOneTree(10) #Takes in the depth of the tree you want to plot

# --------------------------------------------
# Task 12:
# --------------------------------------------
'''
OpeningsN = OpeningManagement(gameList)

#Gives you the openings played more than n (given in parameter) times
#print(OpeningsN.lookAtNOpenings(500))

#Gives you openings played more than n times and their results ('Opening', [white wins, draws, black wins])
#print(OpeningsN.getResultForNOpenings(100)) 

dokument = HTMLFile(gameList, 20)  # takes in gameList and n. n = openings played more than n times in the table for black and white
dokument.createFile() #Creates the HTML-file for the document'''

'''
We need to give N in the parameter together with gameList when creating the 
HTMLFile(Document) object. 
You also have to change or create a new HTMLFile-object to change n.
The document/report creates a document.html file that you can open to view the report.
This document also contains all the plots and tables specified in the 
earlier tasks. It's also important to remember that you need to run
the plots function or have them already in the folder by running the plots functions 
earlier in the main file. 
'''





