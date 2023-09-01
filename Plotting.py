# 1. Imported Modules
# -------------------
import numpy as np
import random
import matplotlib.pyplot as plt
import networkx as nx
from Reader import *
from Counter import * 
from tree import *


class Plots:
    def __init__(self, gameList): #A gameList gets determined in the constructor, and all the plotting functions are based on this list
        self.gameList = gameList
    
    def PlotResults(self, resultType): #Type in either "colorWins" or "stockfishWins"
        if resultType == "stockfishWins":
            # creating the dataset
            data1 = CountStockWins(self.gameList)
            data = {'Win':data1[0], 'Draw':data1[1], 'Loss':data1[2]}
            result = list(data.keys())
            values = list(data.values())
            fig = plt.figure(figsize = (10, 5))
            
            # creating the bar plot
            plt.bar(result, values, color ='burlywood', width = 0.4)
            plt.xlabel("Result")
            plt.ylabel("Number of times")
            plt.title("Games won, drawn and lost by Stockfish")
            plt.savefig('plots/' + resultType + ".png")
            plt.show()

        elif resultType == "colorWins":
            # creating the dataset
            whiteData = CountStockResults(self.gameList, "White")
            blackData = CountStockResults(self.gameList, "Black")
            print("White:",whiteData)
            print("Black:",blackData)
            X = ['Win','Draw','Loss']
            X_axis = np.arange(len(X))
            fig = plt.figure(figsize = (10, 5))

            # creating the bar plot
            plt.bar(X_axis - 0.2, whiteData, 0.4, label = 'White', color = "lightgrey")
            plt.bar(X_axis + 0.2, blackData, 0.4, label = 'Black', color = "dimgrey")
            plt.xticks(X_axis, X)
            plt.xlabel("Result")
            plt.ylabel("Number of times")
            plt.title("Games won, drawn and lost by Stockfish based on color")
            plt.legend()
            plt.savefig('plots/' +resultType + ".png")
            plt.show()
        else:
            print("Invalid result type: Type in either 'colorWins' or 'stockfishWins'")

    def PlotOngoning(self):
        list1 = GameLenghts(self.gameList)
        myDict = {}
        for item in list1:
            if item in myDict:
                myDict[item] += 1
            else:
                myDict[item] = 1
        keys = list(myDict.keys())
        values = list(myDict.values())
        
        fig = plt.figure(figsize = (12, 8))
        plt.bar(keys, values)
        plt.title("proportion of games still on-ongoing after 1, 2, 3. . . moves")
        plt.xlabel("Number of moves")
        plt.ylabel("Number of games")
        plt.savefig("plots/OngoingGames.png")
        plt.show()

    def PlotOngoingWhiteAndBlack(self):
        whiteList = GameLenghtsWhite(self.gameList)
        blackList = GameLenghtsBlack(self.gameList)
        myDict = {}
        for item in whiteList:
            if item in myDict:
                myDict[item] += 1
            else:
                myDict[item] = 1
        keys1 = list(myDict.keys())
        values1 = list(myDict.values())
        
        myDict2 = {}
        for item in blackList:
            if item in myDict2:
                myDict2[item] += 1
            else:
                myDict2[item] = 1
        keys2 = list(myDict2.keys())
        values2 = list(myDict2.values())
        
        fig = plt.figure(figsize = (12, 8))
        plt.bar(keys1, values1, label = 'White', color = "sandybrown")
        plt.bar(keys2, values2, label = 'Black', color = "darkcyan")
        plt.title("proportion of games still on-ongoing after 1, 2, 3. . . moves for games played by Stockfish with white pieces and with black pieces.")
        plt.xlabel("Number of moves")
        plt.ylabel("Number of games")
        plt.legend()
        plt.savefig("plots/OngoingGamesWhiteAndBlack.png")
        plt.show()

    def PlotOngoingWinAndLoss(self):
        win = GameLengthsStockfishWin(self.gameList)
        loss = GameLenghtsStockfishLoss(self.gameList)
        myDict = {}
        for item in win:
            if item in myDict:
                myDict[item] += 1
            else:
                myDict[item] = 1
        keys1 = list(myDict.keys())
        values1 = list(myDict.values())
        
        myDict2 = {}
        for item in loss:
            if item in myDict2:
                myDict2[item] += 1
            else:
                myDict2[item] = 1
        keys2 = list(myDict2.keys())
        values2 = list(myDict2.values())
        
        fig = plt.figure(figsize = (12, 8))
        plt.bar(keys1, values1, label = 'Wins', color = "olivedrab")
        plt.bar(keys2, values2, label = 'Losses', color = "coral")
        plt.title("proportion of games still on-ongoing after 1, 2, 3. . . moves for the games won by Stockfish and those Stockfish lost.")
        plt.xlabel("Number of moves")
        plt.ylabel("Number of games")
        plt.legend()
        plt.savefig("plots/OngoingWinAndLoss.png")
        plt.show()
        

    #Tree plot
    def plotOneTree(self, n):
        tree = Tree(self.gameList)
        nodes, edges = tree.NodesAndEdgesToLists()
        n_nodes = n+1
        n_edges = n
        G = nx.Graph()

        # Add nodes to the graph with labels starting at 1
        for n in nodes[:n_nodes]:
            G.add_node(n+1, label = n+1)

        # Add edges to the graph
        for e in edges[:n_edges]:
            G.add_edge(e[0]+1, e[1]+1, weight=e[2])
        color_map = {node: 'lightgray' if node % 2 != 0 else 'dimgrey' for node in G.nodes()}

        # Set the position of each node
        pos = nx.nx_agraph.graphviz_layout(G, prog="dot")

        # Draw the graph
        fig = plt.figure(1, figsize=(12, 8), dpi=100)
        nx.draw(G, node_color=[color_map[node] for node in G.nodes()], pos=pos, with_labels=True, node_size=200, font_size=8, font_weight='bold')

        # Draw edge labels
        edge_labels = nx.get_edge_attributes(G, 'weight')
        
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_size=8, font_weight='bold')
        plt.savefig("plots/plotOneTree.png")
        plt.show()
        
            
        
        
