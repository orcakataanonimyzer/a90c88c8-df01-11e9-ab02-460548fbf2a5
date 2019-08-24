import unittest
import argparse
import wordsearch

class ArgumentParserTest(unittest.TestCase):

    def test_build_argument_parser_returns_an_ArgumentParser(self):
        argument_parser = wordsearch.build_argument_parser()
        assert argument_parser is not None
        assert isinstance(argument_parser, argparse.ArgumentParser)

    def test_ArgumentParser_contains_a_program_name_called_wordsearch(self):
        argument_parser = wordsearch.build_argument_parser()
        assert argument_parser.prog == 'wordsearch'

    def test_ArgumentParser_contains_a_description(self):
        argument_parser = wordsearch.build_argument_parser()
        assert argument_parser.description is not None
        assert argument_parser.description != ''

class SampleTest(unittest.TestCase):

    def test_main(self):
        wordsearch.main()
        assert True
