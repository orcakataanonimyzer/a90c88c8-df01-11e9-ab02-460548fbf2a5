"""Wordsearch is a word search puzzle solver.

This module provides the main entry point of the program and related metadata.

Example:
    To run the program, just do:

        $ python -m wordsearch <FILE>

Attributes:
    __version__ (str): The module's version string.
"""
import argparse

__version__ = '0.1.0'

def build_argument_parser():
    argument_parser = argparse.ArgumentParser(
        prog='wordsearch',
        description='Solves word search puzzles.')
    argument_parser.add_argument(
        'puzzle_file',
        help='The input puzzle file to solve.')
    return argument_parser

def main(argv=None):
    """The main entry point of the program.

    Args:
        argv (:obj:`list` of :obj:`str`): A list of command line arguments.
    """
    argument_parser = build_argument_parser()
    arguments = argument_parser.parse_args()
    print('Hello, world!')

if __name__ == '__main__':
    main()
