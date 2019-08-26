RIGHT = (0,1)
LEFT = (0,-1)
UP = (-1,0)
DOWN = (1,0)
UP_RIGHT = (-1,1)
DOWN_RIGHT = (1,1)
UP_LEFT = (-1,-1)
DOWN_LEFT = (1,-1)
DIRECTIONS = [RIGHT, LEFT, UP, DOWN, UP_RIGHT, DOWN_RIGHT, UP_LEFT, DOWN_LEFT]
MIN_WORD_SIZE = 2

class Puzzle:

    def __init__(self, board):
        if board in [None, [], [[]]]:
            raise ValueError('board is empty.')
        if type(board) is not list:
            raise TypeError('board is not of type list.')
        for row in board:
            if len(row) != len(board):
                raise ValueError('board is not square.')
        if len(board) < MIN_WORD_SIZE:
            raise ValueError('board is too small; it must be at least 2x2.')
        self.board = board

    @property
    def size(self):
        return self.height, self.width

    @property
    def height(self):
        return len(self.board)

    @property
    def width(self):
        return len(self.board[0])

    def position_is_valid(self, position):
        y, x = position
        return 0 <= y < self.height and 0 <= x < self.width

    def all_positions(self):
        for y in range(self.height):
            for x in range(self.width):
                yield (y, x)

    def get_valid_moves(self, position, distance=1):
        if not self.position_is_valid(position):
            raise IndexError('starting position out of bounds.')
        moves = []
        for direction in DIRECTIONS:
            y, x = position
            dy, dx = direction
            y += dy * distance
            x += dx * distance
            if self.position_is_valid((y, x)):
                moves.append((y,x))
        return moves

    def get_direction(self, origin, target):
        if not self.position_is_valid(origin):
            raise IndexError('origin is out of bounds.')
        oy, ox = origin
        ty, tx = target
        y = min(1, max(-1, ty - oy))
        x = min(1, max(-1, tx - ox))
        return y,x

    def get_characters(self, position, target):
        if not self.position_is_valid(position):
            raise IndexError('starting position out of bounds.')
        if not self.position_is_valid(target):
            raise IndexError('target position out of bounds.')
        characters = []
        positions = []
        direction = self.get_direction(position, target)
        while position != target:
            y, x = position
            characters.append(self.board[y][x])
            positions.append(position)
            y += direction[0]
            x += direction[1]
            position = y, x
        y, x = position
        characters.append(self.board[y][x])
        positions.append(position)
        return characters, positions

    def find(self, word):
        for position in self.all_positions():
            for target in self.get_valid_moves(position, distance=len(word)-1):
                characters, positions = self.get_characters(position, target)
                if characters == list(word):
                    return positions
        return []

    def find_all(self, words):
        results = {}
        for word in words:
            positions = self.find(word)
            if positions:
                results[word] = positions
        return results
