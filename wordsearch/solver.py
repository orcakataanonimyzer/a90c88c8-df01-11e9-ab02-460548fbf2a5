"""The :mod:`solver` module contains a set of constants and the :class:`Puzzle`
class that provide a means of easily working with a word search grid represented
as a nested :obj:`list` of characters.

Attributes:
    RIGHT (tuple): A pair of indices (y, x) that represent the minimum number of
        moves necessary to move in the right direction from a given point of
        reference.
    LEFT (tuple): A pair of indices (y, x) that represent the minimum number of
        moves necessary to move in the left direction from a given point of
        reference.
    UP (tuple): A pair of indices (y, x) that represent the minimum number of
        moves necessary to move in the up direction from a given point of
        reference.
    DOWN (tuple): A pair of indices (y, x) that represent the minimum number of
        moves necessary to move in the down direction from a given point of
        reference.
    UP_RIGHT (tuple): A pair of indices (y, x) that represent the minimum number
        of moves necessary to move in the up-right direction from a given point
        of reference.
    DOWN_RIGHT (tuple): A pair of indices (y, x) that represent the minimum
        number of moves necessary to move in the down-right direction from a
        given point of reference.
    UP_LEFT (tuple): A pair of indices (y, x) that represent the minimum number
        of moves necessary to move in the up-left direction from a given point
        of reference.
    DOWN_LEFT (tuple): A pair of indices (y, x) that represent the minimum
        number of moves necessary to move in the down-left direction from a
        given point of reference.
    DIRECTIONS (:obj:`list` of `tuple`): A :obj:`list` of :obj:`tuple`
        containing :attr:`RIGHT`, :attr:`LEFT`, :attr:`UP`, :attr:`DOWN`,
        :attr:`UP_RIGHT`, :attr:`DOWN_RIGHT`, :attr:`UP_LEFT`, and
        :attr:`UP_RIGHT`.
    MIN_WORD_SIZE (int): The minimum word size for a given :class:`Puzzle`.
        This also determines the minimum height and width of a :class:`Puzzle`,
        which are equal.
"""

RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)
UP_RIGHT = (-1, 1)
DOWN_RIGHT = (1, 1)
UP_LEFT = (-1, -1)
DOWN_LEFT = (1, -1)
DIRECTIONS = [RIGHT, LEFT, UP, DOWN, UP_RIGHT, DOWN_RIGHT, UP_LEFT, DOWN_LEFT]
MIN_WORD_SIZE = 2


class Puzzle:
    """The :class:`Puzzle` class provides methods and properties for querying
    and inspecting a word search puzzle.

    Args:
        board (:obj:`list` of :obj:`list` of :obj:`str`): A two-dimensional list
            of single characters that represent the word search puzzle board.

    Raises:
        ValueError: If the specified ``board`` argument is empty or ``None``,
            or if the board is not square in shape (i.e., if the width and
            height are different).
        TypeError: If the board is not of type :obj:`list`.
    """

    def __init__(self, board):
        if board in [None, [], [[]]]:
            raise ValueError('board is empty.')
        if not isinstance(board, list):
            raise TypeError('board is not of type list.')
        for row in board:
            if len(row) != len(board):
                raise ValueError('board is not square.')
        if len(board) < MIN_WORD_SIZE:
            raise ValueError('board is too small; it must be at least 2x2.')
        self.board = board

    @property
    def size(self):
        """tuple: Gives the width and height of the board as a :obj:`tuple` of
        the form ``(height, width)``.
        """
        return self.height, self.width

    @property
    def height(self):
        """int: The height of the board."""
        return len(self.board)

    @property
    def width(self):
        """int: The width of the board."""
        return len(self.board[0])

    def position_is_valid(self, position):
        """Checks the given :obj:`tuple` ``position`` of the form (y, x) or
        (row, col) if it is within the bounds of the board.

        Args:
            position (tuple): A :obj:`tuple` of the form (y, x) or (row, col) to
                be checked for validity.
        """
        # pylint: disable=invalid-name
        y, x = position
        return 0 <= y < self.height and 0 <= x < self.width
        # pylint: enable=invalid-name

    def all_positions(self):
        """A generator that yields the positions in the board.

        Yields:
            tuple: A position as a :obj:`tuple` of the form (y, x) or
            (row, col).

        Examples:
            The following is an example on how to use ``all_positions`` to
            iterate through every position in the board.

            >>> print([pos for pos in puzzle.all_positions()])
            [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        """
        # pylint: disable=invalid-name
        for y in range(self.height):
            for x in range(self.width):
                yield (y, x)
        # pylint: enable=invalid-name

    def get_valid_moves(self, position, distance=1):
        """Gives a list of valid moves from a given ``position`` that are
        ``distance`` spaces away in each direction in :attr:`DIRECTIONS`.

        A move is considerd valid if, starting from the origin ``position``,
        and moving in a direction ``distance`` number of spaces, the resulting
        position is still within the bounds of the board.

        Args:
            position (tuple): A tuple containing a reference point (y, x).
            distance (int): A positive integer that gives the distance from the
                given ``position``.

        Returns:
            :obj:`list` of :obj:`tuple`: A list of valid moves from the point of
            origin, ``position``.

        Raises:
            ValueError: If the distance is not positive.
            IndexError: If the point of origin given by ``position`` is out of
                bounds.
        """
        if distance < 1:
            raise ValueError('distance must be at least 1.')
        if not self.position_is_valid(position):
            raise IndexError('starting position out of bounds.')
        moves = []
        for direction in DIRECTIONS:
            # pylint: disable=invalid-name
            # This allows usage of y and x as variable names.
            y, x = position
            direction_y, direction_x = direction
            y += direction_y * distance
            x += direction_x * distance
            if self.position_is_valid((y, x)):
                moves.append((y, x))
            # pylint: enable=invalid-name
        return moves

    def get_direction(self, origin, target):
        """Determines the relative direction from ``origin`` to ``target``.

        The core idea of this method can be visualized as so.

        The ``origin`` point acts as an anchor, and if one draws a line from
        the ``origin`` to ``target``, the direction of the resulting vector
        gives the relative direction from ``origin`` to ``target``.

        Args:
            origin (tuple): A :obj:`tuple` containing a reference point (y, x).
            target (tuple): A :obj:`tuple` containing a point relative to
                ``origin``.

        Returns:
            tuple: A :obj:`tuple` from the list of :attr:`DIRECTIONS`
            representing the direction one would have to move from the
            ``origin`` to arrive at the ``target``.

        Raises:
            IndexError: if ``origin`` is out of bounds.
        """
        if not self.position_is_valid(origin):
            raise IndexError('origin is out of bounds.')
        origin_y, origin_x = origin
        target_y, target_x = target
        direction_y = min(1, max(-1, target_y - origin_y))
        direction_x = min(1, max(-1, target_x - origin_x))
        return direction_y, direction_x

    def get_characters(self, position, target):
        """Retrieves the characters from the board that fall between the indices
        given in ``position`` and ``target``.

        This method gives both the list of characters and the list of positions
        of each of those characters. The ``position`` and ``target`` are
        specified as tuples giving the (y, x) coordinates for a selection of
        characters.

        Note:
            The results include ``position`` and ``target``. That is to say, the
            range of characters is inclusive.

        Args:
            position (tuple): The start of the range of characters to select.
            target (tuple): The end of the range of characters to select.

        Returns:
            tuple: A :obj:`tuple` that contains a :obj:`list` of characters and
            a :obj:`list` of positions of each character found in the board.

        Raises:
            IndexError: If either ``position`` or ``target`` fall out of the
            bounds of the board.
        """
        if not self.position_is_valid(position):
            raise IndexError('starting position out of bounds.')
        if not self.position_is_valid(target):
            raise IndexError('target position out of bounds.')
        characters = []
        positions = []
        direction = self.get_direction(position, target)
        # pylint: disable=invalid-name
        while position != target:
            y, x = position
            characters.append(self.board[y][x])
            positions.append(position)
            y += direction[0]
            x += direction[1]
            position = y, x
        y, x = position
        characters.append(self.board[y][x])
        # pylint: enable=invalid-name
        positions.append(position)
        return characters, positions

    def find(self, word):
        """Searchs for a ``word`` in the puzzle and gives the positions of the
        characters of that word.

        Args:
            word (str): The word to search in the puzzle.

        Returns:
            A :obj:`list` of :obj:`tuple` of the form (y, x) containing the
            coordinates for each character in the given `word` if it is found
            in the puzzle. Otherwise, an empty :obj:`list` is returned.

        Raises:
            ValueError: If ``word`` is ``None`` or is too long or too short.
            TypeError: If ``word`` is not a :obj:`str`.
        """
        if word is None:
            raise ValueError('the specified word is None.')
        if len(word) > self.width:
            raise ValueError(
                'the specified word (%s) is larger than the board.' % word)
        if len(word) < MIN_WORD_SIZE:
            raise ValueError('the specified word (%s) is too short.' % word)
        if not isinstance(word, str):
            raise TypeError('the specified word is not of type str.')
        for position in self.all_positions():
            for target in self.get_valid_moves(position,
                                               distance=len(word) - 1):
                characters, positions = self.get_characters(position, target)
                if characters == list(word):
                    return positions
        return []

    def find_all(self, words):
        """Searches for each word in the given list of words and gives the
        accumulated results.

        Args:
            words (:obj:`list` of :obj:`str`): A list of words to find in the
                puzzle.

        Returns:
            A :obj:`dict` containing the results of searching for each word in
            the specified list of words.

        Raises:
            ValueError: If ``words`` is ``None``.
            TypeError: If ``words`` is not a :obj:`list`.
        """
        if words is None:
            raise ValueError('the specified list of words is None.')
        if not isinstance(words, list):
            raise TypeError('expected words to be of type list, but got (%s)' %
                            type(words))
        results = {}
        for word in words:
            positions = self.find(word)
            if positions:
                results[word] = positions
        return results
