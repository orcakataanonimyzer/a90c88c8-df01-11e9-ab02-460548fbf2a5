import pytest
import unittest
import argparse
import subprocess
import wordsearch
from wordsearch.solver import Puzzle

PILLAR_SAMPLE_WORD_LIST = 'BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA'.split(',')
# yapf: disable
PILLAR_SAMPLE_PUZZLE_BOARD = [
    ['U','M','K','H','U','L','K','I','N','V','J','O','C','W','E'],
    ['L','L','S','H','K','Z','Z','W','Z','C','G','J','U','Y','G'],
    ['H','S','U','P','J','P','R','J','D','H','S','B','X','T','G'],
    ['B','R','J','S','O','E','Q','E','T','I','K','K','G','L','E'],
    ['A','Y','O','A','G','C','I','R','D','Q','H','R','T','C','D'],
    ['S','C','O','T','T','Y','K','Z','R','E','P','P','X','P','F'],
    ['B','L','Q','S','L','N','E','E','E','V','U','L','F','M','Z'],
    ['O','K','R','I','K','A','M','M','R','M','F','B','A','P','P'],
    ['N','U','I','I','Y','H','Q','M','E','M','Q','R','Y','F','S'],
    ['E','Y','Z','Y','G','K','Q','J','P','C','Q','W','Y','A','K'],
    ['S','J','F','Z','M','Q','I','B','D','B','E','M','K','W','D'],
    ['T','G','L','B','H','C','B','E','C','H','T','O','Y','I','K'],
    ['O','J','Y','E','U','L','N','C','C','L','Y','B','Z','U','H'],
    ['W','Z','M','I','S','U','K','U','R','B','I','D','U','X','S'],
    ['K','Y','L','B','Q','Q','P','M','D','F','C','K','E','A','B']
]
# yapf: enable


class ArgumentParserTest(unittest.TestCase):

    def setup_method(self, method):
        self.sample_puzzle = 'data/pillar-sample.puzzle'
        self.argument_parser = wordsearch.build_argument_parser()

    def test_build_argument_parser_returns_an_ArgumentParser(self):
        assert self.argument_parser is not None
        assert isinstance(self.argument_parser, argparse.ArgumentParser)

    def test_ArgumentParser_contains_a_program_name_called_wordsearch(self):
        assert self.argument_parser.prog == 'wordsearch'

    def test_ArgumentParser_contains_a_description(self):
        assert self.argument_parser.description is not None
        assert self.argument_parser.description != ''

    def test_ArgumentParser_has_a_positional_argument_for_the_input_file(self):
        arguments = self.argument_parser.parse_args([self.sample_puzzle])
        assert 'puzzle_file' in arguments

    def test_ArgumentParser_opens_the_specified_input_file(self):
        arguments = self.argument_parser.parse_args([self.sample_puzzle])
        assert arguments.puzzle_file is not None
        assert not arguments.puzzle_file.closed
        arguments.puzzle_file.close()


class HelpAndUsageTest(unittest.TestCase):

    def setup_method(self, method):
        self.process = subprocess.run('python -m wordsearch -h'.split(),
                                      stdout=subprocess.PIPE)
        self.stdout = self.process.stdout.decode()

    def test_passing_the_help_flag_prints_the_program_usage(self):
        content = 'usage: wordsearch [-h] puzzle_file'
        assert content in self.stdout

    def test_the_help_message_has_a_description_for_the_input_file(self):
        content = 'puzzle_file  The input puzzle file to solve.'
        assert content in self.stdout


class PuzzleParserTest(unittest.TestCase):

    def test_parse_puzzle_returns_the_list_of_words_and_puzzle(self):
        words_list = PILLAR_SAMPLE_WORD_LIST
        puzzle_matrix = PILLAR_SAMPLE_PUZZLE_BOARD
        with open('data/pillar-sample.puzzle') as puzzle_file:
            words, puzzle = wordsearch.parse_puzzle(puzzle_file)
        assert words == words_list
        assert puzzle == puzzle_matrix

    def test_parse_puzzle_returns_the_puzzle_contained_in_the_input_file(self):
        # yapf: disable
        puzzle_matrix = [
            ['M','R','P','P','O','N','E','P','Y','T','H','O','N','C','J'],
            ['X','X','D','W','R','R','N','G','S','U','X','Q','D','Q','P'],
            ['C','L','A','V','L','M','W','P','A','E','Z','B','E','G','T'],
            ['F','O','E','J','S','F','Y','Z','E','U','A','E','D','M','Y'],
            ['H','T','Y','X','S','Y','F','P','S','P','G','R','S','T','M'],
            ['G','N','I','M','M','A','R','G','O','R','P','N','C','H','S'],
            ['Z','R','K','L','K','E','O','O','L','Z','L','E','A','H','A'],
            ['E','H','T','V','L','I','E','T','V','B','P','T','Q','L','T'],
            ['A','D','D','Z','G','W','Y','W','E','S','Y','T','N','U','F'],
            ['X','Q','Z','W','W','Z','T','Q','R','J','H','I','P','W','N'],
            ['M','U','O','H','K','L','G','K','Z','H','J','R','P','F','N'],
            ['P','R','I','C','Z','R','N','K','G','H','R','W','L','Z','V'],
            ['D','E','S','F','J','C','T','T','X','G','D','P','Q','J','F'],
            ['F','R','Y','O','J','V','T','K','X','Z','G','N','H','B','O'],
            ['A','O','G','K','U','P','F','Q','A','M','Y','L','W','I','M']
        ]
        # yapf: enable
        with open('data/sample-puzzle.puzzle') as puzzle_file:
            words, puzzle = wordsearch.parse_puzzle(puzzle_file)
        assert puzzle == puzzle_matrix

    def test_parse_puzzle_returns_the_word_list_in_the_input_file(self):
        word_list = [
            'LANGUAGE', 'PROGRAMMING', 'PUZZLE', 'PYTHON', 'SEARCH', 'SOLVER',
            'THE', 'WORD', 'WRITTEN'
        ]
        with open('data/sample-puzzle.puzzle') as puzzle_file:
            words, puzzle = wordsearch.parse_puzzle(puzzle_file)
        assert words == word_list

    def test_parse_puzzle_raises_value_error_if_puzzle_file_is_null(self):
        with pytest.raises(ValueError) as e:
            assert wordsearch.parse_puzzle(None)
        assert str(e.value) == 'Invalid argument: puzzle_file must not be None.'

    def test_parse_puzzle_returns_none_and_empty_list_if_puzzle_is_empty(self):
        with open('data/empty.puzzle') as puzzle_file:
            words, puzzle = wordsearch.parse_puzzle(puzzle_file)
        assert words is None
        assert puzzle == []


class ParsePuzzleFromCommandLineArgument(unittest.TestCase):
    """Tests the integration between the argument parser and puzzle parser."""

    def test_parse_puzzle_from_command_line_argument(self):
        argument_parser = wordsearch.build_argument_parser()
        arguments = argument_parser.parse_args(['data/pillar-sample.puzzle'])
        words, puzzle = wordsearch.parse_puzzle(arguments.puzzle_file)
        assert words is not None
        assert words == PILLAR_SAMPLE_WORD_LIST
        assert puzzle != []
        assert puzzle == PILLAR_SAMPLE_PUZZLE_BOARD


class OutputFormatTest(unittest.TestCase):

    def test_format_results_returns_a_formatted_string(self):
        results = {
            'BONES': [(6, 0), (7, 0), (8, 0), (9, 0), (10, 0)],
            'KHAN': [(9, 5), (8, 5), (7, 5), (6, 5)],
            'KIRK': [(7, 4), (7, 3), (7, 2), (7, 1)],
            'SCOTTY': [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)],
            'SPOCK': [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)],
            'SULU': [(3, 3), (2, 2), (1, 1), (0, 0)],
            'UHURA': [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
        }
        words = PILLAR_SAMPLE_WORD_LIST
        formatted_text = wordsearch.format_results(results, words)
        # yapf: disable
        expected = '\n'.join([
            'BONES: (0,6),(0,7),(0,8),(0,9),(0,10)',
            'KHAN: (5,9),(5,8),(5,7),(5,6)',
            'KIRK: (4,7),(3,7),(2,7),(1,7)',
            'SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)',
            'SPOCK: (2,1),(3,2),(4,3),(5,4),(6,5)',
            'SULU: (3,3),(2,2),(1,1),(0,0)',
            'UHURA: (4,0),(3,1),(2,2),(1,3),(0,4)'
        ])
        # yapf: enable
        assert expected == formatted_text


class SolverIntegrationTest(unittest.TestCase):
    """Test the integration between the main application and the solver module.
    """

    def setup_method(self, method):
        self.puzzle_file = open('./data/pillar-sample.puzzle')
        self.words, self.board = wordsearch.parse_puzzle(self.puzzle_file)
        self.puzzle = Puzzle(self.board)

    def teardown_method(self, method):
        self.puzzle_file.close()

    def test_can_load_a_file_and_solve_the_puzzle(self):
        actual = self.puzzle.find_all(self.words)
        expected = {
            'BONES': [(6, 0), (7, 0), (8, 0), (9, 0), (10, 0)],
            'KHAN': [(9, 5), (8, 5), (7, 5), (6, 5)],
            'KIRK': [(7, 4), (7, 3), (7, 2), (7, 1)],
            'SCOTTY': [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)],
            'SPOCK': [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)],
            'SULU': [(3, 3), (2, 2), (1, 1), (0, 0)],
            'UHURA': [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
        }
        assert expected == actual


class WordsearchEndToEndTest(unittest.TestCase):
    """Tests the entire application end-to-end."""

    def setup_method(self, method):
        self.path = './data/pillar-sample.puzzle'
        self.command = 'python -m wordsearch %s' % self.path
        self.process = subprocess.run(self.command.split(),
                                      stdout=subprocess.PIPE)
        self.stdout = self.process.stdout.decode()

    def test_wordsearch_solves_the_input_puzzle_file(self):
        # yapf: disable
        expected = '\n'.join([
            'BONES: (0,6),(0,7),(0,8),(0,9),(0,10)',
            'KHAN: (5,9),(5,8),(5,7),(5,6)',
            'KIRK: (4,7),(3,7),(2,7),(1,7)',
            'SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)',
            'SPOCK: (2,1),(3,2),(4,3),(5,4),(6,5)',
            'SULU: (3,3),(2,2),(1,1),(0,0)',
            'UHURA: (4,0),(3,1),(2,2),(1,3),(0,4)'
        ])
        # yapf: enable
        assert expected in self.stdout
