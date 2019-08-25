import pytest
import unittest

from wordsearch.solver import Puzzle

class PuzzleTest(unittest.TestCase):

    def setup_method(self, method):
        # Word list: dog, cat, pig
        self.board = [
            ['x', 'd', 'o', 'g'],
            ['o', 'r', 't', 'i'],
            ['j', 'a', 'i', 'p'],
            ['c', 'l', 'm', 'q']
        ]
        self.puzzle = Puzzle(self.board)

    def test_raises_an_exception_if_the_board_is_null(self):
        with pytest.raises(ValueError) as e:
            puzzle = Puzzle(None)
        assert str(e.value) == 'board is empty.'

    def test_raises_an_exception_if_the_board_is_an_empty_list(self):
        with pytest.raises(ValueError) as e:
            puzzle = Puzzle([])
        assert str(e.value) == 'board is empty.'

    def test_raises_an_exception_if_the_board_is_empty(self):
        with pytest.raises(ValueError) as e:
            puzzle = Puzzle([[]])
        assert str(e.value) == 'board is empty.'

    def test_raises_an_exception_if_board_is_not_a_list(self):
        with pytest.raises(TypeError) as e:
            puzzle = Puzzle({})
        assert str(e.value) == 'board is not of type list.'

    def test_raises_an_exception_if_the_board_is_not_square(self):
        board = [
            ['a', 'b', 'c'],
            ['e', 'f'],
            ['g', 'h', 'i']
        ]
        with pytest.raises(ValueError) as e:
            puzzle = Puzzle(board)
        assert str(e.value) == 'board is not square.'

    def test_raises_an_exception_if_the_board_is_not_at_least_2x2(self):
        board = [['a']]
        with pytest.raises(ValueError) as e:
            puzzle = Puzzle(board)
        assert str(e.value) == 'board is too small; it must be at least 2x2.'

    def test_size(self):
        assert (4,4) == self.puzzle.size()

    def test_all_positions_is_an_iterator_through_the_entire_board(self):
        positions = [position for position in self.puzzle.all_positions()]
        expected = [(0, 0),(0, 1),(0, 2),(0, 3),(1, 0),(1, 1),(1, 2),(1, 3),
                    (2, 0),(2, 1),(2, 2),(2, 3),(3, 0),(3, 1),(3, 2),(3, 3)]
        assert expected == positions
