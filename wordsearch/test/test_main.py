import unittest
import argparse
import wordsearch

class ArgumentParserTest(unittest.TestCase):

    def test_build_argument_parser_returns_an_ArgumentParser(self):
        argument_parser = wordsearch.build_argument_parser()
        assert argument_parser is not None
        assert isinstance(argument_parser, argparse.ArgumentParser)

class SampleTest(unittest.TestCase):

    def test_main(self):
        wordsearch.main()
        assert True
