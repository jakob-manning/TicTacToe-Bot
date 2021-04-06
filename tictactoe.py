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
    # Count the number of turns left
    turnsLeft = 0
    for row in board:
        turnsLeft += row.count(EMPTY)
    if turnsLeft % 2 == 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    emptySquares = set()
    #for every row and every column check if it is empty
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                emptySquares.add((i,j))
    return emptySquares
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # if move is invalid - raisse an exception
    i, j = action
    if board[i][j] != EMPTY:
        raise ValueError
    ## return a new board object via a deepcopy
    newboard = copy.deepcopy(board)
    newboard[i][j] = player(board)
    return newboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for row in board:
        if row[0] != EMPTY and row[0] == row[1] == row[2]:
            return row[0]
    # check columns
    if board[0][0] != EMPTY and board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] != EMPTY and board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] != EMPTY and board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    # check diagonals
     # check columns
    if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check if someone has won
    currentWinner = winner(board)
    if currentWinner != None :
        return True

    # check if the board is full
    for row in board:
        for column in row:
            if column == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winningPlayer = winner(board)
    if winningPlayer == X:
        return 1
    if winningPlayer == O:
        return -1
    return 0

def getScore(board):
    if terminal(board):
        return utility(board)
    
    availableMoves = actions(board)

    currentPlayer = player(board)
    bestScore = 0
    if currentPlayer == X:
            # maximize
            bestScore = -1
    if currentPlayer == O:
        # minimize
        bestScore = 1
    for move in availableMoves:
        nextBoard = result(board, move)
        nextScore = getScore(nextBoard)
        #check current player before deciding whether to maximize or minimize
        if currentPlayer == X:
            # maximize
            if nextScore > bestScore:
                bestScore = nextScore
        if currentPlayer == O:
            # minimize
            if nextScore < bestScore:
                bestScore = nextScore
    return bestScore


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    currentPlayer = player(board)

    possibleMoves = actions(board)

    bestScore = 0
    if currentPlayer == X:
            # maximize
            bestScore = -1
    if currentPlayer == O:
        # minimize
        bestScore = 1
    bestMove = None
    for move in possibleMoves:
        ## Call my special scoring function
        # generate action
        resultingBoard = result(board, move)
        # get score of new board
        score = getScore(resultingBoard)
        # check if we've won
        if terminal(resultingBoard):
            if winner(resultingBoard) == currentPlayer:
                return move
        # check if new board is better than best score
        if currentPlayer == X:
            # maximize
            if score > bestScore:
                score = bestScore
                bestMove = move
        if currentPlayer == O:
            # minimize
            if score < bestScore:
                score = bestScore
                bestMove = move
    
    #check if there is no best move
    if bestMove == None:
        bestMove = possibleMoves.pop()

    return bestMove

    """
    take a board, use actions() to find all possible moves
     - for each of those check terminal status
     - if not terminal find all possible moves from that board

    if 

    """

