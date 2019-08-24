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
        self.process = subprocess.run(
            'python -m wordsearch -h'.split(),
            stdout=subprocess.PIPE)
        self.stdout = self.process.stdout.decode()

    def test_passing_the_help_flag_prints_the_program_usage(self):
        content = 'usage: wordsearch [-h] puzzle_file'
        assert content in self.stdout

    def test_the_help_message_has_a_description_for_the_input_file(self):
        content = 'puzzle_file  The input puzzle file to solve.'
        assert content in self.stdout
