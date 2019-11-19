from board import Board

current_player = 1
playing_x = 0
player_one = ''
player_two = ''

"""
0 = nothing
1 = X
2 = O
"""
current_board = Board()

def main():
    init()
    while True:
        game_logic()

def end_game():
    print('O Jogo acabou!')
    exit()

def game_logic():
    isValid = True
    while isValid:
        pos = int(input("Player %s position? (1-9): " %(str(current_player))))
        isValid = not validPlay(pos) # only stops asking when it's valid
    makePlay(pos)

    if current_board.is_over():
        end_game()
        
    switchPlayer()
    current_board.print()

def get_avaible_positions():
    # TODO
    pass

def makePlay(pos):
    playerLetter = getCurrentPlayLetter()
    setPosInMatrix(pos, playerLetter)

def validPlay(pos):
    if pos < 1 or pos > 9:
        return False
    if getPosInMatrix(pos) != 0:
        return False
    return True

def getCurrentPlayLetter():
    if playing_x == current_player: # se o jogador atual for o mesmo que estiver jogando com o X, retorna X, senao Bola
        return 1
    return 2

def getPosInMatrix(pos):
    if pos == 1:
        return current_board.matrix[0][0]
    if pos == 2:
        return current_board.matrix[0][1]
    if pos == 3:
        return current_board.matrix[0][2]
    if pos == 4:
        return current_board.matrix[1][0]
    if pos == 5:
        return current_board.matrix[1][1]
    if pos == 6:
        return current_board.matrix[1][2]
    if pos == 7:
        return current_board.matrix[2][0]
    if pos == 8:
        return current_board.matrix[2][1]
    if pos == 9:
        return current_board.matrix[2][2]

def setPosInMatrix(pos, value):
    if pos == 1:
        current_board.matrix[0][0] = value
    if pos == 2:
        current_board.matrix[0][1] = value
    if pos == 3:
        current_board.matrix[0][2] = value
    if pos == 4:
        current_board.matrix[1][0] = value
    if pos == 5:
        current_board.matrix[1][1] = value
    if pos == 6:
        current_board.matrix[1][2] = value
    if pos == 7:
        current_board.matrix[2][0] = value
    if pos == 8:
        current_board.matrix[2][1] = value
    if pos == 9:
        current_board.matrix[2][2] = value

def init():
    global playing_x
    global player_one
    global player_two
    player_one = input("Player 1 name: ")
    player_two = input("Player 2 name: ")
    playing_x = int(input("Who's playing with X? (1/2): "))

def switchPlayer():
    global current_player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

if __name__ == "__main__":
    main()