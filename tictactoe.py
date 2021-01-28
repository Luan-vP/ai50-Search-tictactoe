"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

empty_board = [[None, None, None],
                [None, None, None],
                [None, None, None]]

one_move = [["X", None, None],
                [None, None, None],
                [None, None, None]]

two_moves = [["X", None, None],
                [None, "O", None],
                [None, None, None]]

full_board_no_win = [["X", "O", "X"],
                    ["X", "O", "X"],
                    ["O", "X", "O"]]
                
full_board_X_wins = [["X", "X", "X"],
                    ["X", "O", "O"],
                    ["O", "X", "O"]]

full_board_O_wins = [["O", "X", "X"],
                    ["X", "O", "X"],
                    ["X", "O", "O"]]

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    move_count = 0

    for row in board:
        for space in row:
            if space is not None:
                move_count +=1

    if move_count % 2 == 0:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    for row in board:
        for space in row:
            if space is None:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # for max player

    # if terminal, return utility
    # else v = -inf
    # then loop over possible actions looking for one which provides max value

    #min and max call each other recursively. Just like a real game between humans
    raise NotImplementedError
