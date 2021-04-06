# scrap.py

X = "X"
O = "O"
EMPTY = None

board = [[X, O, EMPTY], [O, EMPTY, EMPTY], [X, EMPTY, X]]

x = board[0].count(EMPTY)

x += board[0].count(EMPTY)

    
import tictactoe as ttt

playerTurn = ttt.player(board)
availableSquares = ttt.actions(board)

a = availableSquares.pop()

# newState = ttt.result(board, (2,1))
# newState = ttt.result(newState, (2,0))
# winningTeam = ttt.winner(newState)

victoryBoard = [[X, X, EMPTY], [X, EMPTY, EMPTY], [X, EMPTY, EMPTY]]

winningTeam = ttt.winner(victoryBoard)
terminalCheck = ttt.terminal(victoryBoard)

utilityStatus = ttt.utility(victoryBoard)
# utilityStatus = ttt.utility(newState)

bestMove = ttt.minimax(board)
