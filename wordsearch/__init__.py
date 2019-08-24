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
    if puzzle_file is None:
        raise ValueError('Invalid argument: puzzle_file must not be None.')
    words = None
    puzzle = []
    for line in puzzle_file:
        # By splitting on nothing, the string is split on white space.
        # The combination of splitting and joining like this is used to remove
        # all white space (like the \n at the end of each line).
        line = ''.join(line.split()).split(',')
        if words is None:
            words = line
        else:
            puzzle.append(line)
    return words, puzzle

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
