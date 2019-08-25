class Puzzle:

    def __init__(self, board):
        if board in [None, [], [[]]]:
            raise ValueError('board is empty.')
        if type(board) is not list:
            raise TypeError('board is not of type list.')
        for row in board:
            if len(row) != len(board):
                raise ValueError('board is not square.')
        if len(board) < 2:
            raise ValueError('board is too small; it must be at least 2x2.')
        self.board = board

    def size(self):
        return len(self.board),len(self.board[0])

    def all_positions(self):
        height, width = self.size()
        for y in range(height):
            for x in range(width):
                yield (y, x)
