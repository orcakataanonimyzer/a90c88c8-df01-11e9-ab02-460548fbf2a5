import unittest
import argparse
import subprocess
import wordsearch


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
        assert arguments.puzzle_file == self.sample_puzzle


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
        words_list = 'BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA'.split(',')
        puzzle_matrix = [
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
        with open('data/pillar-sample.puzzle') as puzzle_file:
            words, puzzle = wordsearch.parse_puzzle(puzzle_file)
        assert words == words_list
        assert puzzle == puzzle_matrix
