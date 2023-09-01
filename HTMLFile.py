from Reader import *
from Plotting import *
from Counter import *
from OpeningManagement import *

gameList = Reader_ImportChessDataBase("Stockfish_15_64-bit.commented.[2600].pgn", 2600)

class HTMLFile:
    def __init__(self, gameList, n): #The constructor takes in a gameList. This gameList is used for the statistics that'll be in tables and pictures in the document. Also it creates an empty body and head alongside some other variables that'll gets internally to create the document with the createFile function
        self.documentName = '''Report'''
        self.head = None
        self.body = None
        self.contentBody = ''''''
        self.htmlstart = '''<html>'''
        self.htmlend = '''</html>'''
        self.title = ''''''
        self.style = ''''''
        self.tablestart = "<table>"
        self.tableend = "</table>"
        self.gameList = gameList
        self.OpeningManagementObject = OpeningManagement(gameList)
        self.n = n #Will include tables for black and white for openings played more than n times. The parameter is determined by the analyst when creating the HTMLFile-object

    def createHead(self): #This creates the head of the document. It includes the style to give the tables borders + the title of the document. 
        self.title = '''<title>''' + self.documentName + '''</title>'''
        self.style = '''<style>table, th, td {border: 1px solid;}</style>'''
        self.head = '''<html><head>''' + self.title + self.style + '''<html></head>'''
    
    def createBody(self): #The structure of the document. Here all the other table, image, paragraph and heading functions are placed to become the content of the body. It does this by creating a large HTML string that becomes the body of the HTML-file
        bodyStart = self.htmlstart + '''<body>'''
        bodyEnd = '''</body>''' + self.htmlend
        self.createLargeHeading(self.documentName)
        self.createSmallerHeading("Stockfish statistics")
        #PlottingObject = Plots(self.gameList)
        #PlottingObject.PlotResults("stockfishWins")
        #PlottingObject.PlotResults("colorWins")
        self.insertImage("plots/stockfishWins.png", "This graph shows the amount of wins, draws and losses stockfish has")
        self.insertImage("plots/colorWins.png", "This shows the amount of wins, draws and losses of stockfish has for all colors")
        self.createSmallerHeading("Stockfish Table")
        self.createStockResultTable()
        self.createParagraph("This table shows the specific amount of wins Stockfish has with all colors and in total")
        #PlottingObject.PlotOngoning()
        self.createSmallerHeading("Plots for stockfish ongoing games")
        self.insertImage("plots/OngoingGames.png", "This plot shows the proportion of ongoing games after 1, 2, 3, ... moves")
        #PlottingObject.PlotOngoingWhiteAndBlack()
        self.insertImage("plots/OngoingGamesWhiteAndBlack.png", "This shows the proportion of ongoing games after 1, 2, 3, ... moves played by stockfish with black and white pieces")
        #PlottingObject.PlotOngoingWinAndLoss()
        self.insertImage("plots/OngoingWinAndLoss.png", "This plot shows the proportion of ongoing games after n moves played by stockfish where it won or lost")
        self.createSmallerHeading("Mean and Standard deviation table for moves")
        self.createMovesMeanStdTable()
        self.createParagraph("This is the table for standard deviation and mean for 1, 2, 3, ... moves in ongoing games for stockfish. The table shows the mean and std where stockfish played with white, black, those it won, those it lost and all games in general")
        self.createSmallerHeading("Stockfish opening results")
        self.insertImage("plots/plotOneTree.png", "This graph shows the tree plot with 1/2 moves at a given depth")
        self.CreateOpeningTable(self.n)
        self.createParagraph("This shows two tables for openings, one for black and one for white. First it's the opening results in the table for games by white, and then it's the results in the table for games played by black")
        self.body = bodyStart + self.contentBody + bodyEnd
    
    def createLargeHeading(self, headingTitle): #Creates a large heading with the spesified title in the parameter 
        self.contentBody +=  '''<h1>''' + headingTitle + '''</h1>'''
    
    def createSmallerHeading(self, headingTitle): #Creates a smaller heading. Used for some headings throughout the document
        self.contentBody +=  '''<h3>''' + headingTitle + '''</h3>'''
    
    def createParagraph(self, paragraphContent): #Creates a default paragraph that can be used in the document
        self.contentBody += '''<p>''' + paragraphContent + '''<p>'''

    def createStockResultTable(self): #Creates the stockfish win, draw and loss table for when it's played with both white and black + in total
        stats_white = CountStockResults(self.gameList, "White")
        stats_black = CountStockResults(self.gameList, "Black")
        total_result = []
        for i in range(0, len(stats_white)):
            total_result.append(stats_white[i] + stats_black[i])
        row1 = self.createRowInTable("Win","Draw", "Loss", "headerStock")
        row2 = self.createRowInTable(str(stats_white[0]), str(stats_white[1]), str(stats_white[2]), "White")
        row3 = self.createRowInTable(str(stats_black[0]), str(stats_black[1]), str(stats_black[2]), "Black")
        row4 = self.createRowInTable(str(total_result[0]), str(total_result[1]), str(total_result[2]), "Total")
        self.contentBody += self.tablestart + row1 + row2 + row3 + row4 + self.tableend
    


    def createMovesMeanStdTable(self): #Creates the mean and standard deviation table for moves in games
        std = getStandardDeviationMoves(self.gameList)
        mean = getMeanMoves(self.gameList)
        row1 = self.createRowInTable("", "Mean","Standard deviation", "headerStd")
        row2 = self.createRowInTable("Ongoing moves for all games" ,str(round(mean, 2)), str(round(std, 2)), "std")
        row3 = self.createRowInTable("Ongoing moves for games in wins for white", str(round(getMeanMoveWhiteBlack(self.gameList)[0],2)), str(round(getStandardDeviationWhiteBlack(self.gameList)[0],2)), "std")
        row4 = self.createRowInTable("Ongoing moves for games in wins for black", str(round(getMeanMoveWhiteBlack(self.gameList)[1],2)), str(round(getStandardDeviationWhiteBlack(self.gameList)[1],2)), "std")
        row5 = self.createRowInTable("Ongoing moves for games where stockfish won", str(round(getMeanMoveWinLoss(self.gameList)[0],2)), str(round(getStandardDeviationWinLoss(self.gameList)[0],2)), "std")
        row6 = self.createRowInTable("Ongoing moves for games where stockfish lost", str(round(getMeanMoveWinLoss(self.gameList)[1],2)), str(round(getStandardDeviationWinLoss(self.gameList)[1],2)), "std")
        self.contentBody += self.tablestart + row1 + row2 + row3 + row4 + row5 + row6 + self.tableend

    
    def createRowInTable(self, Colum1, Colum2, Colum3, version): #Creates a row in a table. The version determines which row it is
        row_start = "<tr>"
        row_end = "</tr>"
        if version == "headerStock":
            return row_start + "<th>" + "</th>" + "<th>" + Colum1 + "</th>" + "<th>" + Colum2 + "</th>"+ "<th>" + Colum3 + "</th>"+ row_end
        elif version == "headerStd":
            return row_start + "<th>" + Colum1 + "</th>" + "<th>" + Colum2 + "</th>"+ "<th>" + Colum3 + "</th>"+ row_end
        elif version == "std":
            return row_start + "<td>" + Colum1 + "</td>" + "<td>" + Colum2 + "</td>" + "<td>" + Colum3 + "</td>" + row_end
        elif version == "White":
            return row_start + "<td>"+ "White" +"</td>" + "<td>" + Colum1 + "</td>" + "<td>" + Colum2 + "</td>"+ "<td>" +Colum3 + "</td>"+ row_end
        elif version == "Total":
            return row_start + "<td>"+ "Total" +"</td>" + "<td>" + Colum1 + "</td>" + "<td>" + Colum2 + "</td>"+ "<td>" +Colum3 + "</td>"+ row_end
        elif version == "Black":
            return row_start + "<td>"+ "Black" +"</td>" + "<td>" + Colum1 + "</td>" + "<td>" + Colum2 + "</td>"+ "<td>" +Colum3 + "</td>"+ row_end

    def createRowOpening(self, Opening, Colum1, Colum2, Colum3): #Used as a template for creating the rows in the white and black opening tables
        row_start = "<tr>"
        row_end = "</tr>"
        return row_start + "<td>"+ Opening +"</td>" + "<td>" + Colum1 + "</td>" + "<td>" + Colum2 + "</td>"+ "<td>" +Colum3 + "</td>"+ row_end

        
    def createDocument(self): #Creates the head and body of the document
        self.createHead()
        self.createBody()
        return self.head + self.title + self.body
    
    def createFile(self): #Creates the HTML-File
        content = self.createDocument()
        document = open('''document.html''', '''w''')
        document.write(content)
        document.close()

    def insertImage(self, image, figureText): #Insert the spesified image with the figure text into the document
        self.contentBody += '<figure><img src="' + image + '"' + '"width="460" height="345"/><figcaption>' + figureText + '</figcation></figure>'
    
    def openingResultRows(self, n): #Returns the rows for the opening results for black and white that's been played more than n times
        OpeningResultWhite, OpeningResultBlack = self.OpeningManagementObject.getResultForNOpenings(n)
        whiteRows = []
        blackRows = []
        for i in range(0, len(OpeningResultWhite)):
            whiteRows.append(self.createRowOpening(OpeningResultWhite[i][0],str(OpeningResultWhite[i][1][0]), str(OpeningResultWhite[i][1][1]), str(OpeningResultWhite[i][1][2])))
        for i in range(0, len(OpeningResultBlack)):
            blackRows.append(self.createRowOpening(OpeningResultBlack[i][0],str(OpeningResultBlack[i][1][0]), str(OpeningResultBlack[i][1][1]), str(OpeningResultBlack[i][1][2])))
        return whiteRows, blackRows
    
    def CreateOpeningTable(self, n): #Returns the table for the opening results for black and white that's been played more than N times
        whiteRows, blackRows = self.openingResultRows(n)

        #Creates the opening table for white
        self.contentBody += self.tablestart + self.createRowInTable("Win", "Draw", "Loss", "White")
        for i in range(0, len(whiteRows)):
            self.contentBody += whiteRows[i]
        self.contentBody += self.tableend

        #Creates the opening table for black
        self.contentBody += self.tablestart + "<br></br>" + self.createRowInTable("Win", "Draw", "Loss", "Black")
        for i in range(0, len(blackRows)):
            self.contentBody += blackRows[i]
        self.contentBody += self.tableend
        
        
