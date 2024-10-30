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
    Returns starting state of the board.0
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    board_1dimension = [cell for row in board for cell in row]

    x_count = board_1dimension.count(X)
    o_count = board_1dimension.count(O)

    if o_count < x_count:
        return O
    return X


def actions(board):

    actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            position = board[i][j]
            if position == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    row, cell = action
    actionsi = actions(board)
    if action not in actionsi:
        raise ValueError("Ação inválida")

    new_board = copy.deepcopy(board)

    player_turn = player(board)
    new_board[row][cell] = player_turn
    return new_board


def winner(board):

    # horizoltal check
    for cell in board:
        if cell[0] == cell[1] == cell[2] and cell[0] != EMPTY:
            return cell[0]

    # vertical check
    for row in range(len(board)):
        if board[0][row] == board[1][row] == board[2][row] and board[0][row] != EMPTY:
            return board[0][row]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):

    onedimension_board = [cell for row in board for cell in row]
    if EMPTY in onedimension_board and not winner(board):
        return False
    return True


def utility(board):

    won = winner(board)
    if won:
        if won == X:
            return 1
        return -1
    return 0


def max_value(state, alpha, beta):
    if terminal(state):
        return utility(state), None

    best_action = None
    for action in actions(state):
        new_state = result(state, action)
        state_value, _ = min_value(new_state, alpha, beta)
        if state_value > beta:
            beta = state_value
            best_action = action
        if beta >= alpha:
            break
    return beta, best_action


def min_value(state, alpha, beta):
    if terminal(state):
        return utility(state), None

    best_action = None
    for action in actions(state):
        new_state = result(state, action)
        state_value, _ = max_value(new_state, alpha, beta)
        if state_value < alpha:
            alpha = state_value
            best_action = action
        if alpha <= beta:
            break
    return alpha, best_action


def minimax(board):
    if terminal(board):
        return None

    alpha = math.inf
    beta = -math.inf

    if player(board) == 'X':
        _, action = max_value(board, alpha, beta)
    else:
        _, action = min_value(board, alpha, beta)

    return action
