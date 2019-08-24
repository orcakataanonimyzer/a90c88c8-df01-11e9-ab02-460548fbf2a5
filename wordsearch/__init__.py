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

def parse_puzzle(puzzle_file):
    words = 'BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA'.split(',')
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
    return words, puzzle_matrix

def build_argument_parser():
    """Constructs and configures an :obj:`argparse.ArgumentParser`.

    The parser is configured with the program name, description, and a
    positional argument for the input file.

    Returns:
        A configured instance of :obj:`argparse.ArgumentParser`.
    """
    argument_parser = argparse.ArgumentParser(
        prog='wordsearch', description='Solves word search puzzles.')
    argument_parser.add_argument('puzzle_file',
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
