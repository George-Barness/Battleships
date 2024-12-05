#https://ele.exeter.ac.uk/pluginfile.php/4304197/mod_label/intro/Computer%20Science%20Programming%20-%20Battleship%20Coursework%202024-25.pdf
from flask import Flask, render_template, jsonify, request
from components import *
from mp_game_engine import *
import pandas as pd

app = Flask(__name__)

ai_ships = create_battleships()
player_ships = create_battleships()
ai_board_empty = Initialise_board()
player_board_empty = Initialise_board()

@app.route('/placement', methods=['GET','POST'])
def placement_interface():
    if request.method == "GET":
        board = Initialise_board()
        ships = create_battleships()
        return render_template('placement.html', ships=ships, board_size=len(board)) #we can either use ai ships or player ships because they both have the same ships
    elif request.method == 'POST':
        global data
        data = request.get_json()
        return jsonify({'message': 'Received'}), 200

@app.route('/', methods=['GET'])
def root():
    if request.method == "GET":
        global ai_board, player_board 
        ai_board = place_battleships(ai_board_empty, ai_ships, "Random")
        try:
            player_board_empty = Initialise_board()
            player_board = place_battleships(player_board_empty, player_ships, "Custom", data)
            return render_template('main.html', player_board=player_board)
        except:
            player_board_empty = Initialise_board()
            player_board = place_battleships(player_board_empty, player_ships, "Custom")
            return render_template('main.html', player_board=player_board)


@app.route('/attack', methods=['GET'])
def process_attack():
    if request.method == "GET":
        x = request.args.get('x')
        y = request.args.get('y')
        hit = attack((x,y), ai_board, ai_ships) 
        coords = generate_attack()
        attack(coords, player_board, player_ships)
        if all  (ship == 0 for ship in ai_ships.values()) == True: #if player sinks all ai ships
            return jsonify({'hit': hit,
            'AI_Turn': coords,
            'finished': "Game Over Player wins"
            })
        elif all(ship == 0 for ship in player_ships.values()) == True: #if ai sinks all player ships
            return jsonify({'hit': hit,
            'AI_Turn': coords,
            'finished': "Game Over AI wins"
            })
        else:  
            return jsonify({'hit': hit,
            'AI_Turn': coords,
            })
    

if __name__ == '__main__':  
    app.run()