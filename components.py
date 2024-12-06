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
        battleships[battleship[0]] = int(battleship[1])
    return battleships

def place_battleships(board:list, ships:dict, argument="Simple", data=None): #we pass through data for the cusotm placement in main.py
    if argument == "Simple":
        row = 0
        for ship in ships:
            if int(ships[ship]) > len(board):
                pass
            else:
                for i in range(int(ships[ship])):
                    board[row][i] = ship
                row += 1
    elif argument == "Random":
        for ship in ships:
            if int(ships[ship]) > len(board): #if size of ship is bigger than board then dont place
                pass
            else:
                valid = False
                while valid != True: #have to check if ships collides with already placed ship
                    orientation = random.choice(["v", "h"]) #randomly select 
                    if orientation == "v":  
                        row = random.randrange(0, (len(board)-int(ships[ship]) + 1)) #need to add one because randrange is exclusive in upper bound
                        col = random.randrange(0, len(board))
                        if all(board[row + i][col] is None for i in range(ships[ship])) == True: #check if any ships in way of ship
                            for i in range (ships[ship]): #place ship
                                board[row + i][col] = ship
                                valid = True
                    else:           
                        col = random.randrange(0, (len(board)-int(ships[ship]) + 1))
                        row = random.randrange(0, len(board))
                        if all(board[row][col + i] is None for i in range(ships[ship])) == True: #check if any ships in way of ship
                            for i in range (ships[ship]): #place ship
                                board[row][col + i] = ship
                                valid = True   
    elif argument == "Custom":
        if data:
            pass
        else:
            f = open("placement.json", "r")
            data = json.load(f)
        for i in data:
            pos = data[i]
            if pos[2] == "h":
                for j in range(int(ships[i])):
                    board[int(pos[1])][int(pos[0]) + j] = i
            elif pos[2] == "v":
                for j in range(int(ships[i])):
                    board[int(pos[1]) + j][int(pos[0])] = i
    return board


board = Initialise_board()
ships = create_battleships()
x = place_battleships(board, ships, "Random")
print(pd.DataFrame(x))
