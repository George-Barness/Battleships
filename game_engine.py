from components import *
def attack(coordinates:tuple, board, battleships):
    try:
        if board[int(coordinates[1])][int(coordinates[0])] == None:
            return False    
        else:  
            ship = board[int(coordinates[1])][int(coordinates[0])]
            if ship:
                battleships[ship] = int(battleships[ship]) - 1
                board[int(coordinates[1])][int(coordinates[0])] = None
                if battleships[ship] == 0:
                    print("sunk")  
            return True
    except:
        pass

def cli_coordinates_input():
    coordinates = tuple(input("Enter coordinates of attack: ").strip('()').split(','))
    return coordinates

def simple_game_loop():
    print("Welcome to the game!")
    board = Initialise_board()
    ships = create_battleships()
    place_battleships(board, ships)
    game_over = False
    while game_over != True:
        coordinates = cli_coordinates_input()
        if attack(coordinates, board, ships) == True:
            print("hit")
            if all(ship == 0 for ship in ships.values()) == True:
                game_over = True
        else:
            print("no hit")
    print("GAME OVER")


if __name__ == "__main__":
    simple_game_loop()