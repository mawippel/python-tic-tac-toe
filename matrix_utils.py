def get_pos_is_matrix(current_board, pos):
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

def set_pos_in_matrix(current_board, pos, value):
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