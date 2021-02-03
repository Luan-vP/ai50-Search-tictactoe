"""
Tic Tac Toe Player
"""

import math
import copy

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
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                possible_actions.add((i,j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    row = action[0]
    column = action[1]

    if board[row][column] is not None:
        raise "Invalid action - square is occupied"

    new_board = copy.deepcopy(board)
    new_board[row][column] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row[0] == row[1] and row[1] == row[2]:
            return row[0]

    for column in zip(*board):
        if column[0] == column[1] and column[1] == column[2]:
            return column[0]
    
    # Check diagonals
    if ( board[0][0] == board[1][1] and board[1][1] == board[2][2] ) or ( board[0][2] == board[1][1] and board[1][1] == board[2][0] ):
        return board[1][1]

    return None
 

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board):
        return True

    # Check for full board
    for row in board:
        for space in row:
            if space is None:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)

    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def max_value(board):
    """
    Returns highest possible value for a game state
    """
    
    # if terminal, return utility
    if terminal(board):
        return utility(board)
    
    v = -1000

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    """
    Returns highest possible value for a game state
    """
    
    # if terminal, return utility
    if terminal(board):
        return utility(board)
    
    v = 1000

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # if terminal, return utility
    if terminal(board):
        return None

    if player(board) == X:
        # for max player

        v = -1000
        current_best_action = None
        
        for action in actions(board):

            # Find move with highest value of minß_value(board, action)
            action_score = min_value(result(board, action))

            if action_score > v:
                v = action_score
                current_best_action = action
        
        return current_best_action

    else:
        # for min player

        v = 1000
        current_best_action = None
        
        for action in actions(board):

            # Find move with smallest value of max_value(board, action)
            action_score = max_value(result(board, action))

            if action_score < v:
                v = action_score
                current_best_action = action
        
        return current_best_action