class Board:

    """
        0 = nothing
        1 = X
        2 = O
    """
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    def print(self):
        for line in self.matrix:
            print(' %s | %s | %s \n' % (line[0], line[1], line[2]))
            print('---+---+---')

    def is_over(self):
        return self.horizontal() or self.vertical() or self.diagonal()

    def horizontal(self):
        for line in self.matrix:
            if line[0] == line[1] and line[1] == line[2] and line[0] != 0 and line[1] != 0 and line[2] != 0:
                return True
        return False

    def vertical(self):
        for i in range(3):
            if self.matrix[0][i] == self.matrix[1][i] and self.matrix[1][i] == self.matrix[2][i] and self.matrix[0][i] != 0 and self.matrix[1][i] != 0 and self.matrix[2][i] != 0:
                return True
        return False

    def diagonal(self):
        if self.matrix[0][0] == self.matrix[1][1] and self.matrix[1][1] == self.matrix[2][2] and self.matrix[0][0] != 0 and self.matrix[1][1] != 0 and self.matrix[2][2] != 0:
            return True
        if self.matrix[0][1] == self.matrix[1][1] and self.matrix[1][1] == self.matrix[2][0] and self.matrix[0][1] != 0 and self.matrix[1][1] != 0 and self.matrix[2][0] != 0:
            return True
        return False
