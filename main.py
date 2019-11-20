from board import Board
from matrix_utils import *

current_player = 1
playing_x = 0
player_one = ''
player_two = ''

current_board = Board()

def init():
    global playing_x
    global player_one
    global player_two
    player_one = input("Player 1 name: ")
    player_two = input("Player 2 name: ")
    playing_x = int(input("Who's playing with X? (1/2): "))

def end_game():
    print('Game Over!')
    print('Congratulations Player %s' %(current_player))
    exit()

def game_logic():
    isValid = True
    while isValid:
        pos = int(input("Player %s position? (1-9): " %(str(current_player))))
        isValid = not valid_play(pos) # only stops asking when it's valid
    make_play(pos)

    if current_board.is_over():
        end_game()
        
    switch_player()
    current_board.print()

def get_avaible_positions():
    # TODO
    pass

def make_play(pos):
    playerLetter = get_current_player_letter()
    set_pos_in_matrix(current_board, pos, playerLetter)

def valid_play(pos):
    if pos < 1 or pos > 9:
        return False
    if get_pos_is_matrix(current_board, pos) != 0:
        return False
    return True

def get_current_player_letter():
    if playing_x == current_player:
        return 1
    return 2


def switch_player():
    global current_player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

def main():
    init()
    while True:
        game_logic()

if __name__ == "__main__":
    main()