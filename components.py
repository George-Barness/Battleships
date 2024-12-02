import random
import json
import pandas as pd

def Initialise_board(size = 10):
    board = [[None for i in range(size)] for j in range(size)] #change to None
    return board

def create_battleships(filename = "battleships.txt"):
    f = open(filename, "r")
    battleships = {}
    for line in f:
        battleship = line.rstrip('\n').split(":")
        battleships[battleship[0]] = battleship[1]
    return battleships

def place_battleships(board:list, ships:dict, argument="Simple"):
    row = 0
    if argument == "Simple":
        for ship in ships:
            if int(ships[ship]) > len(board):
                pass
            else:
                for i in range(int(ships[ship])):
                    board[row][i] = ship
                row += 1
    elif argument == "Random":
        for ship in ships:
            if int(ships[ship]) > len(board):
                pass
            else:
                valid = False
                while valid != True:
                    orientation = random.choice(["v", "h"])
                    if orientation == "v":  
                        row = random.randrange(0, (len(board)-int(ships[ship])))
                        col = random.randrange(0, len(board)-1)
                        for i in range(int(ships[ship])):
                            if board[row + i][col] == None:
                                board[row + i][col] = ship
                            else:
                                for j in range(i):
                                    board[row + i][col] = None
                                break                        
                    else:
                        col = random.randrange(0, (len(board)-int(ships[ship])))
                        row = random.randrange(0, len(board)-1)
                        for i in range(int(ships[ship])):
                            if board[row][col + i] == None:
                                board[row][col + i] = ship
                            else:
                                for j in range(i):
                                    board[row][col + i] = None
                                break    
                    valid = True
    elif argument == "Custom":
        f = open("placement.json", "r")
        data = json.load(f)
        for i in data:
            pos = data[i]
            if pos[2] == "h":
                for j in range(int(ships[i])):
                    board[int(pos[0])][int(pos[1]) + j] = i
            elif pos[2] == "v":
                for j in range(int(ships[i])):
                    board[int(pos[0]) + j][int(pos[1])] = i
    return board


board = Initialise_board()
ships = create_battleships()
x = place_battleships(board, ships)
