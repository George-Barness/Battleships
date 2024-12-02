import random
from components import *
from game_engine import *

players = {}
used_coords = []

def generate_attack(size=10):
    while True:
        col = random.randrange(0, size) #randrange is inclusive first lower bound and exclusive upper bound so we dont need to do size-1
        row = random.randrange(0, size)
        coords = (row,col)
        if coords not in used_coords:
            used_coords.append(coords)
            return coords

def ai_opponent_game_loop():
    print("Welcome to the game!")

    ai_board_empty = Initialise_board()
    ai_ships = create_battleships()
    ai_board = place_battleships(ai_board_empty, ai_ships, "Random")
    
    player_board_empty = Initialise_board()
    player_ships = create_battleships()
    player_board = place_battleships(player_board_empty, player_ships, "Custom")
    
    print(pd.DataFrame(ai_board))
    players["player"] = [player_board, player_ships]
    players["ai"] = [ai_board, ai_ships]
    game_over = False
    while game_over != True:
        print(pd.DataFrame(player_board))
        player_coords = cli_coordinates_input()
        hit = attack(player_coords, ai_board, ai_ships)
        if hit == True:
            print("hit")
            if all(ship == 0 for ship in ai_ships.values()) == True:
                print("Player wins")
                game_over = True
        else:
            print("miss")
        ai_coords = generate_attack()
        hit = attack(ai_coords, player_board, player_ships)
        if hit == True:
            print("hit")
            if all(ship == 0 for ship in player_ships.values()) == True:
                print("AI wins")
                game_over = True
        else:
            print("miss")

