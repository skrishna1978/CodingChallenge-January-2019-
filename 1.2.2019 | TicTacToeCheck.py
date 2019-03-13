#2.1.2019 - Given a 3x3 array for a Tic-Tac-Toe game, check the state of the board via a function.
#Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty,
#1 if it is an "X", or 2 if it is an "O", like so:
#-1 if the board is not yet finished (there are empty spots),
#1 if "X" won,
#2 if "O" won,
#0 if it's a cat's game (i.e. a draw).

def checkState(board): #2d array sent in
  for i in range(0,3): #loop from 0 until 3 for i
    if board[i][0] == board[i][1] == board[i][2] != 0: #if none of the rows contain 0s, return what exists in entire row aka winner
      return board[i][0]
    elif board[0][i] == board[1][i] == board[2][i] != 0: #if none of the columns contains 0s, return what exists in entire col aka winner
      return board[0][i]
      
  if board[0][0] == board[1][1] == board[2][2] != 0: #if left diagonal doesn't contains 0s, return what exists in diagonal, aka winner 
    return board[0][0]
  elif board[0][2] == board[1][1] == board[2][0] != 0: #same for right diagonal
    return board[0][0]

  elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
    return 0 #for a draw, aka no one won
  else:
    return -1 #0s exist, aka game not finished yet.

    

#check function
board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]
print(checkState(board)) #0s exist so it will return -1
board = [[0, 0, 2],
         [0, 1, 2],
         [2, 1, 2]]
print(checkState(board)) #O has won so it will return 2
