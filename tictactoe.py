"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

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
    
    for row in board:
        if row[0] == row[1] and row[1] == row[2]:
            return 1 if row[0] == "X" else -1

    for column in zip(*board):
        if column[0] == column[1] and column[1] == column[2]:
            return 1 if column[0] == "X" else -1
    
    # Check diagonals
    if ( board[0][0] == board[1][1] and board[1][1] == board[2][2] ) or ( board[0][2] == board[1][1] and board[1][1] == board[2][0] ):
        return 1 if board[1][1] == "X" else -1

    return 0


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
