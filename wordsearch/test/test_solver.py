import pytest
import unittest

import wordsearch.solver
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

    def test_size_returns_the_width_and_height_as_a_tuple(self):
        assert (4,4) == self.puzzle.size

    def test_height_returns_the_height_of_the_board(self):
        assert 4 == self.puzzle.height

    def test_width_returns_the_width_of_the_board(self):
        assert 4 == self.puzzle.width

    def test_all_positions_is_an_iterator_through_the_entire_board(self):
        positions = [position for position in self.puzzle.all_positions()]
        expected = [(0, 0),(0, 1),(0, 2),(0, 3),(1, 0),(1, 1),(1, 2),(1, 3),
                    (2, 0),(2, 1),(2, 2),(2, 3),(3, 0),(3, 1),(3, 2),(3, 3)]
        assert expected == positions

    def test_get_valid_moves_returns_a_list_of_valid_moves(self):
        current_position = (0,0)
        moves = self.puzzle.get_valid_moves(current_position)
        assert wordsearch.solver.RIGHT in moves
        assert wordsearch.solver.DOWN in moves
        assert wordsearch.solver.DOWN_RIGHT in moves

    def test_get_valid_moves_does_not_return_invalid_moves(self):
        current_position = (3,3)
        moves = self.puzzle.get_valid_moves(current_position)
        assert wordsearch.solver.RIGHT not in moves
        assert wordsearch.solver.DOWN not in moves
        assert wordsearch.solver.DOWN_RIGHT not in moves

    def test_get_valid_moves_projects_multiple_spaces(self):
        current_position = (0,0)
        moves = self.puzzle.get_valid_moves(current_position, distance=3)
        assert (0,3) in moves
        assert (3,0) in moves
        assert (3,3) in moves

        current_position = (2, 1)
        moves = self.puzzle.get_valid_moves(current_position, distance=3)
        assert not moves

        current_position = (2, 1)
        moves = self.puzzle.get_valid_moves(current_position, distance=2)
        assert len(moves) == 3
        assert (0,1) in moves
        assert (2,3) in moves
        assert (0,3) in moves

        current_position = (3, 3)
        moves = self.puzzle.get_valid_moves(current_position, distance=3)
        assert (0,0) in moves
        assert (0,3) in moves
        assert (3,0) in moves

    def test_get_direction_returns_the_direction_from_origin_to_target(self):
        direction = self.puzzle.get_direction((3,0),(0,3))
        assert wordsearch.solver.UP_RIGHT == direction

        direction = self.puzzle.get_direction((0,0), (1,1))
        assert wordsearch.solver.DOWN_RIGHT == direction

    def test_get_characters_returns_characters_in_the_given_range(self):
        characters, positions = self.puzzle.get_characters((0,1), (0,3))
        assert 'dog' == ''.join(characters)

        characters, positions = self.puzzle.get_characters((2,3), (0,3))
        assert 'pig' == ''.join(characters)

        characters, positions = self.puzzle.get_characters((3,0), (1,2))
        assert 'cat' == ''.join(characters)

    def test_get_characters_returns_the_positions_in_the_given_range(self):
        characters, positions = self.puzzle.get_characters((0,1), (0,3))
        assert [(0,1),(0,2),(0,3)] == positions

        characters, positions = self.puzzle.get_characters((2,3), (0,3))
        assert [(2,3),(1,3),(0,3)] == positions

        characters, positions = self.puzzle.get_characters((3,0), (1,2))
        assert [(3,0),(2,1),(1,2)] == positions
