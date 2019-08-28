import unittest
import pytest

import wordsearch.solver
from wordsearch.solver import Puzzle


class PuzzleTest(unittest.TestCase):

    def setup_method(self, method):
        # Word list: dog, cat, pig
        # yapf: disable
        self.board = [
            ['x', 'd', 'o', 'g'],
            ['o', 'r', 't', 'i'],
            ['j', 'a', 'i', 'p'],
            ['c', 'l', 'm', 'q']
        ]
        # yapf: enable
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
        # yapf: disable
        board = [
            ['a', 'b', 'c'],
            ['e', 'f'],
            ['g', 'h', 'i']
        ]
        # yapf: enable
        with pytest.raises(ValueError) as e:
            puzzle = Puzzle(board)
        assert str(e.value) == 'board is not square.'

    def test_raises_an_exception_if_the_board_is_not_at_least_2x2(self):
        board = [['a']]
        with pytest.raises(ValueError) as e:
            puzzle = Puzzle(board)
        assert str(e.value) == 'board is too small; it must be at least 2x2.'

    def test_size_returns_the_width_and_height_as_a_tuple(self):
        assert (4, 4) == self.puzzle.size

    def test_height_returns_the_height_of_the_board(self):
        assert 4 == self.puzzle.height

    def test_width_returns_the_width_of_the_board(self):
        assert 4 == self.puzzle.width

    def test_all_positions_is_an_iterator_through_the_entire_board(self):
        positions = [position for position in self.puzzle.all_positions()]
        expected = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2),
                    (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1),
                    (3, 2), (3, 3)]
        assert expected == positions

    def test_get_valid_moves_returns_a_list_of_valid_moves(self):
        current_position = (0, 0)
        moves = self.puzzle.get_valid_moves(current_position)
        assert wordsearch.solver.RIGHT in moves
        assert wordsearch.solver.DOWN in moves
        assert wordsearch.solver.DOWN_RIGHT in moves

    def test_get_valid_moves_does_not_return_invalid_moves(self):
        current_position = (3, 3)
        moves = self.puzzle.get_valid_moves(current_position)
        assert wordsearch.solver.RIGHT not in moves
        assert wordsearch.solver.DOWN not in moves
        assert wordsearch.solver.DOWN_RIGHT not in moves

    def test_get_valid_moves_projects_multiple_spaces(self):
        current_position = (0, 0)
        moves = self.puzzle.get_valid_moves(current_position, distance=3)
        assert (0, 3) in moves
        assert (3, 0) in moves
        assert (3, 3) in moves

        current_position = (2, 1)
        moves = self.puzzle.get_valid_moves(current_position, distance=3)
        assert not moves

        current_position = (2, 1)
        moves = self.puzzle.get_valid_moves(current_position, distance=2)
        assert len(moves) == 3
        assert (0, 1) in moves
        assert (2, 3) in moves
        assert (0, 3) in moves

        current_position = (3, 3)
        moves = self.puzzle.get_valid_moves(current_position, distance=3)
        assert (0, 0) in moves
        assert (0, 3) in moves
        assert (3, 0) in moves

    def test_get_valid_moves_raises_error_if_distance_is_zero_or_negative(self):
        with pytest.raises(ValueError) as e:
            self.puzzle.get_valid_moves((0, 0), distance=-1)
        assert str(e.value) == 'distance must be at least 1.'

    def test_get_valid_moves_raises_error_if_position_is_out_of_bounds(self):
        with pytest.raises(IndexError) as e:
            self.puzzle.get_valid_moves((-1, 0), distance=1)
        assert str(e.value) == 'starting position out of bounds.'

        with pytest.raises(IndexError) as e:
            self.puzzle.get_valid_moves((0, -1), distance=1)
        assert str(e.value) == 'starting position out of bounds.'

        with pytest.raises(IndexError) as e:
            self.puzzle.get_valid_moves((4, 3), distance=1)
        assert str(e.value) == 'starting position out of bounds.'

        with pytest.raises(IndexError) as e:
            self.puzzle.get_valid_moves((3, 4), distance=1)
        assert str(e.value) == 'starting position out of bounds.'

    def test_get_direction_returns_the_direction_from_origin_to_target(self):
        direction = self.puzzle.get_direction((3, 0), (0, 3))
        assert wordsearch.solver.UP_RIGHT == direction

        direction = self.puzzle.get_direction((0, 0), (1, 1))
        assert wordsearch.solver.DOWN_RIGHT == direction

    def test_get_direction_returns_zero_zero_if_target_is_origin(self):
        assert (0, 0) == self.puzzle.get_direction((2, 2), (2, 2))

    def test_get_direction_raises_error_if_origin_is_out_of_bounds(self):
        with pytest.raises(IndexError) as e:
            self.puzzle.get_direction((-1, 0), (2, 2))
        assert str(e.value) == 'origin is out of bounds.'

    def test_get_characters_returns_characters_in_the_given_range(self):
        characters, positions = self.puzzle.get_characters((0, 1), (0, 3))
        assert 'dog' == ''.join(characters)

        characters, positions = self.puzzle.get_characters((2, 3), (0, 3))
        assert 'pig' == ''.join(characters)

        characters, positions = self.puzzle.get_characters((3, 0), (1, 2))
        assert 'cat' == ''.join(characters)

    def test_get_characters_returns_the_positions_in_the_given_range(self):
        characters, positions = self.puzzle.get_characters((0, 1), (0, 3))
        assert [(0, 1), (0, 2), (0, 3)] == positions

        characters, positions = self.puzzle.get_characters((2, 3), (0, 3))
        assert [(2, 3), (1, 3), (0, 3)] == positions

        characters, positions = self.puzzle.get_characters((3, 0), (1, 2))
        assert [(3, 0), (2, 1), (1, 2)] == positions

    def test_get_characters_raises_error_if_position_out_of_bounds(self):
        with pytest.raises(IndexError) as e:
            self.puzzle.get_characters((-1, 0), (2, 0))
        assert str(e.value) == 'starting position out of bounds.'

    def test_get_characters_raises_error_if_target_out_of_bounds(self):
        with pytest.raises(IndexError) as e:
            self.puzzle.get_characters((2, 0), (-1, 0))
        assert str(e.value) == 'target position out of bounds.'

    def test_find_returns_an_empty_list_if_the_word_cannot_be_found(self):
        assert [] == self.puzzle.find('cow')

    def test_find_returns_the_positions_of_the_characters_in_the_word(self):
        assert [(0, 1), (0, 2), (0, 3)] == self.puzzle.find('dog')
        assert [(2, 3), (1, 3), (0, 3)] == self.puzzle.find('pig')
        assert [(3, 0), (2, 1), (1, 2)] == self.puzzle.find('cat')

    def test_find_raises_value_error_if_word_is_null(self):
        with pytest.raises(ValueError) as e:
            self.puzzle.find(None)
        assert str(e.value) == 'the specified word is None.'

    def test_find_raises_value_error_when_word_is_larger_than_puzzle(self):
        word = 'moose'
        with pytest.raises(ValueError) as e:
            self.puzzle.find(word)
        assert str(e.value) == \
            'the specified word (%s) is larger than the board.' % word

    def test_find_raises_value_error_when_word_is_too_short(self):
        with pytest.raises(ValueError) as e:
            self.puzzle.find('d')
        assert str(e.value) == 'the specified word (%s) is too short.' % 'd'

    def test_find_raises_type_error_if_word_is_not_a_str(self):
        word = ['c', 'a', 't']
        with pytest.raises(TypeError) as e:
            self.puzzle.find(word)
        assert str(e.value) == 'the specified word is not of type str.'

    def test_find_all_returns_an_empty_dict_if_no_words_could_be_found(self):
        assert {} == self.puzzle.find_all(['cow'])

    def test_find_all_retuns_a_dict_with_the_positions_of_each_word(self):
        words = ['dog', 'cat', 'pig']
        expected = {
            'dog': [(0, 1), (0, 2), (0, 3)],
            'cat': [(3, 0), (2, 1), (1, 2)],
            'pig': [(2, 3), (1, 3), (0, 3)]
        }
        assert expected == self.puzzle.find_all(words)

    def test_find_all_raises_value_error_when_words_is_null(self):
        with pytest.raises(ValueError) as e:
            self.puzzle.find_all(None)
        assert str(e.value) == 'the specified list of words is None.'

    def test_find_all_raises_type_error_if_words_is_not_a_list(self):
        words = ('cat', 'dog', 'pig')
        with pytest.raises(TypeError) as e:
            self.puzzle.find_all(words)
        assert str(e.value) == \
            'expected words to be of type list, but got (%s)' % type(words)
