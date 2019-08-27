"""Wordsearch is a word search puzzle solver.

This module provides the main entry point of the program and related metadata.

Example:
    To run the program, just do:

        $ python -m wordsearch <FILE>

Attributes:
    __version__ (str): The module's version string.
"""
import argparse

from wordsearch.solver import Puzzle

__version__ = '0.1.0'


def format_results(results, words):
    """Formats the `results` for each word in `words`.

    The results are received as a dict mapping a word to the positions of the
    characters of that word in the puzzle. The list of words is provided as a
    second argument to control the order that the results should be printed in.

    This function assumes that the coordinates of each character are in the form
    (y,x) and will reverse them accordingly so they are output as a typical
    (x,y) coordinate pair.

    Args:
        results (dict): A :obj:`dict` containing the results of a solved word
            search puzzle.
        words (list): A :obj:`list` of :obj:`str` containing the list of words
            that exist in the results.

    Returns:
        A formatted :obj:`str` with each word and position of each character in
        the word as a pair of indices (x,y) where x is the column and y is the
        row where the character was found.
    """
    strings = []
    for word in words:
        positions = ','.join(['(%s,%s)' % (x, y) for y, x in results[word]])
        strings.append('%s: %s' % (word, positions))
    return '\n'.join(strings)


def parse_puzzle(puzzle_file):
    """Parses a puzzle file, producing a list of words and puzzle board.

    Reads the contents of the open :obj:`file object`, and creates a list of
    words and a puzzle board. It is assumed that the first line of the file is
    a comma separated list of words to be searched for in the puzzle board. The
    puzzle board is assumed to be a square matrix of characters. Each row is on
    its own line (immediately after the first line) and each character is
    separated with a comma.

    Example:
        The following is an example of the expected input. The first line is a
        comma separated list of words followed by a 15x15 matrix of characters.
    ::

        BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA
        U,M,K,H,U,L,K,I,N,V,J,O,C,W,E
        L,L,S,H,K,Z,Z,W,Z,C,G,J,U,Y,G
        H,S,U,P,J,P,R,J,D,H,S,B,X,T,G
        B,R,J,S,O,E,Q,E,T,I,K,K,G,L,E
        A,Y,O,A,G,C,I,R,D,Q,H,R,T,C,D
        S,C,O,T,T,Y,K,Z,R,E,P,P,X,P,F
        B,L,Q,S,L,N,E,E,E,V,U,L,F,M,Z
        O,K,R,I,K,A,M,M,R,M,F,B,A,P,P
        N,U,I,I,Y,H,Q,M,E,M,Q,R,Y,F,S
        E,Y,Z,Y,G,K,Q,J,P,C,Q,W,Y,A,K
        S,J,F,Z,M,Q,I,B,D,B,E,M,K,W,D
        T,G,L,B,H,C,B,E,C,H,T,O,Y,I,K
        O,J,Y,E,U,L,N,C,C,L,Y,B,Z,U,H
        W,Z,M,I,S,U,K,U,R,B,I,D,U,X,S
        K,Y,L,B,Q,Q,P,M,D,F,C,K,E,A,B

    Args:
        puzzle_file (:obj:`file object`): An open file containing the puzzle to
            be parsed.

    Returns:
        A two-tuple containing the :obj:`list` of words and the puzzle board as
        a square, two-dimensional :obj:`list`.
    """
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
                                 help='The input puzzle file to solve.',
                                 type=argparse.FileType('r', encoding='UTF-8'))
    return argument_parser


def main():
    """The main entry point of the program."""
    argument_parser = build_argument_parser()
    arguments = argument_parser.parse_args()
    words, board = parse_puzzle(arguments.puzzle_file)
    arguments.puzzle_file.close()
    puzzle = Puzzle(board)
    print(format_results(puzzle.find_all(words), words))


if __name__ == '__main__':
    main()
