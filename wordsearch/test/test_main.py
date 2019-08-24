import unittest
import argparse
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

class SampleTest(unittest.TestCase):

    def test_main(self):
        wordsearch.main()
        assert True
