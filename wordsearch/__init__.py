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
    return argparse.ArgumentParser()

def main(argv=None):
    """The main entry point of the program.

    Args:
        argv (:obj:`list` of :obj:`str`): A list of command line arguments.
    """
    print('Hello, world!')

if __name__ == '__main__':
    main()
